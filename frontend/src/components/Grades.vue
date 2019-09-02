<template>
    <div id="grade">
        <v-container app>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-card-text>
                            <v-icon>insert_chart</v-icon>
                            <div class="title">Grades</div>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>

            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-breadcrumbs :items="breadcrumb" divider=">"/>
                    </v-card>
                </v-flex>
            </v-layout>

            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-list-item-content>
                            <v-list-item><v-card-text>Select year and semester</v-card-text></v-list-item>
                             <v-list-item>
                            <v-overflow-btn
                                    class="my-2"
                                    :items="years"
                                    label="Year"
                                    v-model="year"
                                    @change="yearSemChange"
                                    target="#dropdown"
                            ></v-overflow-btn>
                                       <v-spacer/>

                            <v-overflow-btn
                                    class="my-2"
                                    :items="semesters"
                                    label="Semester"
                                    v-model="semester"
                                    @change="yearSemChange"
                                    target="#dropdown2"
                            ></v-overflow-btn>

                             </v-list-item>
                        </v-list-item-content>

                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row pb-4>
                <v-flex xs12 md12>
                    <v-card flat>
                        <chart :chart-data="datacollection" :width="8" :height="2" ></chart>

                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-simple-table>
                            <thead>
                            <tr>
                                <th class="text-left">Unit</th>
                                <th class="text-left">Unit Code</th>
                                <th class="text-left">Mid-Term</th>
                                <th class="text-left">Final</th>
                                <th class="text-left">Grade</th>
                                <th class="text-left">Year</th>
                                <th class="text-left">Semester</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="grade in academics">
                                <td>{{grade.course_unit.unit.name}}</td>
                                <td>{{grade.course_unit.unit.code}}</td>
                                <td>{{grade.midterm_mark}}</td>
                                <td>{{grade.final_mark}}</td>
                                <td><v-chip :class="`${grade.grade} white--text my-my2 caption` ">{{grade.grade}}</v-chip></td>
                                <td>{{grade.course_unit.clss.year}}</td>
                                <td>{{grade.course_unit.clss.semester}}</td>
                            </tr>
                            </tbody>
                        </v-simple-table>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>
<script>
    import axios from 'axios'
    import Chart from '../chart';

    export default {
        components: {Chart},
        data() {
            return {
                breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/',
                    },
                    {
                        text: 'Grades',
                        disabled: true,
                        href: 'breadcrumbs_dashboard',
                    },
                ],
                years: [],
                semesters: [],
                year: "",
                semester: "",
                academics: null,
                datacollection: '',

            }
        },

        methods: {
            yearSemChange() {
                this.getAcademics();

            },


            getAcademics() {
                var p = this;
                var url = "/academics/grades/?";

                if (this.year) {
                    var y = this.year;
                    url = `${url}year=${y}`;

                    if (this.semester) {
                        var s = this.semester;
                        url = `${url}&semester=${s}`;
                    }
                }

                axios.get(url).then(function ({data}) {

                    for (var i = 0; i < data.length; i++) {
                        var item = data[i];
                        var year = item.course_unit.clss.year;
                        // const unit = item.course_unit.unit.name;
                        // const
                        if (!p.years.includes(year)) {
                            p.years.push(year);
                        }
                        var semester = item.course_unit.clss.semester;
                        if (!p.semesters.includes(semester)) {
                            p.semesters.push(semester);
                        }
                    }
                    p.academics = data;
                });

                axios.get(url).then(response => {
                    const responseData = response.data;
                    this.datacollection = {
                        labels: responseData.map(item => item.course_unit.unit.name),
                        datasets: [
                            {
                                label: 'Grades',
                                backgroundColor: '#3b60e4',
                                data: responseData.map(item => item.final_mark),
                            }
                        ]
                    }
                })
            }


        },


        created() {
            this.getAcademics();
        }
    }

</script>
<style scoped lang="scss">
    .v-chip.A{
        background: #B2FF59
    }
    .v-chip.B{
        background: #8BC34A
    }
    .v-chip.C{
        background: #FFC107
    }
    .v-chip.D{
        background:#FF5722
    }
    .v-chip.E{
        background: #F44336
    }
</style>