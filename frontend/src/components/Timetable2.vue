<template>
    <div id="timetable">
        <v-container>
            <v-layout row>
               <v-flex xs12 md12>
                   <v-card flat>
                       <v-card-text><div class="title">Timetable</div></v-card-text>
                       <v-simple-table>
                           <thead>
                           <tr>
                               <th>Day</th>
                               <th>Class</th>
                               <th>Time</th>
                               <th>Unit</th>
                           </tr>
                           </thead>
                           <tbody>
                                <tr v-for="i in timetable">
                                    <td>{{i.day}}</td>
                                    <td>{{i.venue}}</td>
                                    <td>{{i.start}} - {{i.end}}</td>
                                    <td>{{i.unit.name}}</td>
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
    export default {
        name: 'Timetable2',
        data() {
            return {
                breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/#/',
                    },
                    {
                        text: 'Timetable',
                        disabled: true,
                        href: '/#/Timetable',
                    },
                ],
                day: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                day_model: '',
                tabs:'',
                timetable: null,


            }
        },
        methods: {
              getTimeTable(){
                const p = this;
                axios
                    .get('timetable/')
                    .then(response=>(
                        p.timetable = response.data
                    ))
                    .catch(error=>console.log(error))
            }
        },

        mounted() {
            this.getTimeTable();
        }
    }
</script>
<style></style>