<template>
    <div id="unitdetail">
        <v-container>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-card-text>
                            <v-icon>list</v-icon>
                            <div class="title">Course Details</div>
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
                    <v-card flat class="d-flex align-content-start " v-for="i in unitList">
                        <v-list-item>
                            <v-list-item-content>
                                <div class="overline">{{i.unit.unit.code}}</div>
                                <v-list-item>
                                    <div class="headline">{{i.unit.unit.name}}</div>
                                </v-list-item>
                                <v-list-item>
                                    <v-card-text>
                                        {{i.unit.description}}
                                    </v-card-text>
                                </v-list-item>
                            </v-list-item-content>

                            <v-avatar tile size="150">
                                <v-img :src="i.unit.thumbnail"></v-img>
                            </v-avatar>
                        </v-list-item>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat v-for="i in unitList" flex-wrap>
                        <v-card-text>
                            <div class="title">Unit Instructor</div>
                        </v-card-text>
                        <v-divider/>
                        <v-list-item>
                            <v-avatar tile size="130">
                                <v-img :src="i.unit.lecturer.avatar"></v-img>
                            </v-avatar>
                            <v-list-item-content>

                                <v-list-item>
                                    <div class="headline mb-2">{{i.unit.lecturer.title}} {{i.unit.lecturer.f_name}}
                                        {{i.unit.lecturer.l_name}}
                                    </div>
                                </v-list-item>
                                <v-list-item>
                                    <v-card-text>
                                        {{i.unit.lecturer.bio}}
                                    </v-card-text>
                                </v-list-item>
                                <v-list-item>
                                    <v-icon>
                                        phone
                                    </v-icon>
                                    <v-card-text>{{i.unit.lecturer.phone}}</v-card-text>
                                    <v-spacer></v-spacer>
                                    <v-icon>email</v-icon>
                                    <v-card-text>{{i.unit.lecturer.email}}</v-card-text>
                                </v-list-item>

                            </v-list-item-content>

                        </v-list-item>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-card-text>
                            <div class="title">Course Outline</div>
                        </v-card-text>
                        <v-divider/>
                        <v-expansion-panels :focusable="true" flat>
                            <v-expansion-panel
                                    v-for="i in outline"
                                    :key="i.id"
                            >
                                <v-expansion-panel-header>Week {{i.week}}</v-expansion-panel-header>
                                <v-expansion-panel-content>
                                   {{i.content}}
                                </v-expansion-panel-content>
                            </v-expansion-panel>
                        </v-expansion-panels>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>

    </div>
</template>
<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                unitList: null,
                outline: null,
                breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/',
                    },
                    {
                        text: 'Course',
                        disabled: false,
                        href: '/#/Units',
                    },
                    {
                        text: 'Details',
                        disabled: true,
                        href: '',
                    },
                ],
            }
        },

        methods: {
            getUniDetail() {
                const p = this;
                let url = 'academics/units/?';

                if (this.$route.params.id) {
                    const x = this.$route.params.id;
                    url = `${url}&id=${x}`;
                }
                axios
                    .get(url)
                    .then(response => (
                        p.unitList = response.data
                    ))
                    .catch(error => (console.log(error)))
            },

            getCourseOutline() {
                const p = this;
                let url = 'academics/outline/?';

                if (this.$route.params.id) {
                    const x = this.$route.params.id;
                    url = `${url}&id=${x}`
                }
                axios
                    .get(url)
                    .then(response => (
                        p.outline = response.data
                    ))
                    .catch(error => console.log(error))
            }
        },

        mounted() {
            this.getUniDetail();
            this.getCourseOutline();
        }
    }
</script>
<style>

</style>