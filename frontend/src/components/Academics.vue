<template>
    <div class="academics">
        <v-container fluid>

            <v-layout row>
                <v-flex xs12 md12>
                    <v-card flat outlined>
                        <v-card-text>
                            <div class="title">Academics</div>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
            <!--        BREADCRUMB SHOWING CURRENT DIR-->
            <v-layout row pb-5>
                <v-flex>
                    <v-card flat outlined>
                        <v-flex>
                            <v-breadcrumbs :items="breadcrumb" divider=">"></v-breadcrumbs>
                        </v-flex>
                    </v-card>
                </v-flex>
            </v-layout>
            <!--        TAB ROW-->
            <v-layout row wrap>
                <v-flex wrap>
                    <v-tabs v-model="activeTab">
                        <v-tab v-for="tab in tabs" :key="tab.id" :to="tab.route">{{ tab.name }}</v-tab>

                        <v-tabs-items v-model="activeTab" @change="updateRouter($event)">
                            <v-tab-item v-for="tab in tabs" :key="tab.id" :to="tab.route">
                                <router-view/>
                            </v-tab-item>
                        </v-tabs-items>
                    </v-tabs>

                </v-flex>
            </v-layout>
            <!--        CONTENT -->
            <!--            <v-layout row wrap flat>-->
            <!--                <router-view/>-->
            <!--&lt;!&ndash;                <v-flex>&ndash;&gt;-->
            <!--&lt;!&ndash;                    <v-card flat>&ndash;&gt;-->
            <!--&lt;!&ndash;                        <v-card-text class="title">Courses</v-card-text>&ndash;&gt;-->
            <!--&lt;!&ndash;                        <v-divider></v-divider>&ndash;&gt;-->
            <!--&lt;!&ndash;                        <v-flex xs12 md12 pl-5>&ndash;&gt;-->
            <!--&lt;!&ndash;                             <v-card  pl-10 row>&ndash;&gt;-->

            <!--&lt;!&ndash;                            &lt;!&ndash;    class="mx-auto"&ndash;&gt;&ndash;&gt;-->

            <!--&lt;!&ndash;                            <v-img&ndash;&gt;-->
            <!--&lt;!&ndash;                                    class="white&#45;&#45;text"&ndash;&gt;-->
            <!--&lt;!&ndash;                                    height="200px"&ndash;&gt;-->
            <!--&lt;!&ndash;                                    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"&ndash;&gt;-->
            <!--&lt;!&ndash;                            >&ndash;&gt;-->
            <!--&lt;!&ndash;                                <v-card-title class="align-end fill-height">Top 10 Australian beaches</v-card-title>&ndash;&gt;-->
            <!--&lt;!&ndash;                            </v-img>&ndash;&gt;-->

            <!--&lt;!&ndash;                            <v-card-text>&ndash;&gt;-->
            <!--&lt;!&ndash;                                <span>Number 10</span><br>&ndash;&gt;-->
            <!--&lt;!&ndash;                                <span class="text&#45;&#45;primary">&ndash;&gt;-->
            <!--&lt;!&ndash;                                    <span>Whitehaven Beach</span><br>&ndash;&gt;-->
            <!--&lt;!&ndash;                                    <span>Whitsunday Island, Whitsunday Islands</span>&ndash;&gt;-->
            <!--&lt;!&ndash;                                </span>&ndash;&gt;-->
            <!--&lt;!&ndash;                            </v-card-text>&ndash;&gt;-->

            <!--&lt;!&ndash;                            <v-card-actions>&ndash;&gt;-->
            <!--&lt;!&ndash;                                <v-btn&ndash;&gt;-->
            <!--&lt;!&ndash;                                        text&ndash;&gt;-->
            <!--&lt;!&ndash;                                        color="orange"&ndash;&gt;-->
            <!--&lt;!&ndash;                                >&ndash;&gt;-->
            <!--&lt;!&ndash;                                    Share&ndash;&gt;-->
            <!--&lt;!&ndash;                                </v-btn>&ndash;&gt;-->
            <!--&lt;!&ndash;                                <v-btn&ndash;&gt;-->
            <!--&lt;!&ndash;                                        text&ndash;&gt;-->
            <!--&lt;!&ndash;                                        color="orange"&ndash;&gt;-->
            <!--&lt;!&ndash;                                >&ndash;&gt;-->
            <!--&lt;!&ndash;                                    Explore&ndash;&gt;-->
            <!--&lt;!&ndash;                                </v-btn>&ndash;&gt;-->
            <!--&lt;!&ndash;                            </v-card-actions>&ndash;&gt;-->
            <!--&lt;!&ndash;                        </v-card>&ndash;&gt;-->
            <!--&lt;!&ndash;                        </v-flex>&ndash;&gt;-->

            <!--&lt;!&ndash;                    </v-card>&ndash;&gt;-->
            <!--&lt;!&ndash;                </v-flex>&ndash;&gt;-->
            <!--            </v-layout>-->
        </v-container>

    </div>
</template>
<script>
    export default {
        data() {
            return {
                breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/#/Home',
                    },
                    {
                        text: 'Academics',
                        disabled: true,
                        href: 'breadcrumbs_dashboard',
                    },
                ],
                activeTab: '',
                tabs:[
                    {id:'1', name: 'Courses', route:'Units'},
                    {id:'2', name: 'Grades', route:'Grades'}
                ],
            }
        },
        methods:{
           updateRouter(val){
            this.$router.push(val)
        }
        }
    }
</script>