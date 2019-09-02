<template>
    <v-container fluid>
        <!--    <h1>{{profileInfo}}</h1>-->
        <v-layout row pb-2>
            <v-flex xs12 md12 v-for="i in profileInfo" v-bind:="i.id">
                <v-alert
      color="blue-grey"
      dark
      dense
      icon="school"
      prominent
    >
     Welcome, {{i.first_name}}!
    </v-alert>
<!--                <v-card flat>-->
<!--                    <div class="headline">Welcome, {{i.first_name}}!</div>-->
<!--                </v-card>-->
            </v-flex>
        </v-layout>

        <v-layout row pb-2>
            <v-flex xs12 md12>
                <v-card flat><v-breadcrumbs :items="breadcrumb" divider=">"/></v-card>
            </v-flex>
        </v-layout>

        <v-layout wrap row>
            <v-flex pa-1 xs12 md8>
                <v-card v-for="i in profileInfo" flat>
                    <v-layout-row>
                        <v-card-title>
                           <v-icon>perm_identity</v-icon><div class="headline">Your Profile</div>
                        </v-card-title>
                        <v-divider></v-divider>
                    </v-layout-row>

                    <v-layout-row>
                        <v-list-item>
                            <v-list-item-avatar
                                    tile
                                    size="250"
                                    gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
                            >
                                <v-img :src=i.avatar></v-img>
                            </v-list-item-avatar>
                            <v-list-item-content class="align-self-center">
                                <v-text grey-text> Name: <span class="subtitle-2 pl-1 pb-2">{{i.first_name}} {{i.l_name}}</span>
                                </v-text>
                                <v-text> Registration Number: <span class="subtitle-2 pl-1 pb-1">{{i.registration_number}}</span>
                                </v-text>
                                <v-text> Course: <span
                                        class="subtitle-2 pl-1 pb-1">{{i.course_enrolled.course_name}}</span></v-text>
                                <v-text> Year Enrolled: <span
                                        class="subtitle-2 pl-1 pb-1">{{i.class_enrolled.year}}</span></v-text>
                                <v-text> Semester Enrolled: <span class="subtitle-2 pl-1 pb-1">{{i.class_enrolled.semester}}</span>
                                </v-text>
                            </v-list-item-content>
                        </v-list-item>

                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn class="mx-1" fab outlined color="cyan">
                                <v-icon dark>edit</v-icon>
                            </v-btn>
                        </v-card-actions>
                    </v-layout-row>
                </v-card>
            </v-flex>
           <v-flex xs12 md4 pa-1>
                    <v-card flat>
                        <v-card-text><div class="title">Timetable</div></v-card-text>
                        <v-icon>insert_invitation</v-icon>

                        <v-tabs
                                dark
                                background-color="#3b60e4"
                                show-arrows>
<!--                                :v-for="i in day"-->
<!--                                :key="i"-->
<!--                                :value="tabs"-->
<!--                                v-model="day_model"-->

                            <v-tabs-slider

                          color="teal lighten-2"></v-tabs-slider>

                            <v-tab @change="getMonSchedule">
                                Monday
                            </v-tab>
                            <v-tab @change="getTueSchedule">
                                Tuesday
                            </v-tab>
                            <v-tab @change="getWedSchedule">
                                Wednesday
                            </v-tab>
                            <v-tab @change="getThurSchedule">
                                Thursday
                            </v-tab>
                            <v-tab @change="getFriSchedule">
                                Friday
                            </v-tab>

                            <v-tab-item>
                                <v-card flat  v-for="item in timetable">
                                    <v-list-item-content>
                                        <v-list-item>
                                            <div class="title">{{item.unit.name}}</div>
                                        </v-list-item>
                                         <v-list-item>
                                             <v-icon>access_time</v-icon>
                                             <v-card-text>{{item.start}}-{{item.end}}</v-card-text>
                                         </v-list-item>
                                        <v-list-item>
                                            <v-icon>home</v-icon>
                                            <v-card-text>{{item.venue}}</v-card-text>
                                        </v-list-item>
                                    </v-list-item-content>
                                </v-card>
                            </v-tab-item>
                            <v-tab-item>
                                <v-card flat  v-for="item in timetable">
                                     <v-list-item-content>
                                        <v-list-item>
                                            <div class="title">{{item.unit.name}}</div>
                                        </v-list-item>
                                         <v-list-item>
                                             <v-icon>access_time</v-icon>
                                             <v-card-text>Time: {{item.start}}-{{item.end}}</v-card-text>
                                         </v-list-item>
                                        <v-list-item>
                                            <v-icon>home</v-icon>
                                            <v-card-text>Venue: {{item.venue}}</v-card-text>
                                        </v-list-item>
                                    </v-list-item-content>
                                </v-card>
                            </v-tab-item>
                            <v-tab-item>
                                <v-card flat  v-for="item in timetable">
                                     <v-list-item-content>
                                        <v-list-item>
                                            <div class="title">{{item.unit.name}}</div>
                                        </v-list-item>
                                         <v-list-item>
                                             <v-icon>access_time</v-icon>
                                             <v-card-text>Time: {{item.start}}-{{item.end}}</v-card-text>
                                         </v-list-item>
                                        <v-list-item>
                                            <v-icon>home</v-icon>
                                            <v-card-text>Venue: {{item.venue}}</v-card-text>
                                        </v-list-item>
                                    </v-list-item-content>
                                </v-card>
                            </v-tab-item>
                            <v-tab-item>
                                <v-card flat  v-for="item in timetable">
                                    <v-list-item-content>
                                        <v-list-item>
                                            <div class="title">{{item.unit.name}}</div>
                                        </v-list-item>
                                         <v-list-item>
                                             <v-icon>access_time</v-icon>
                                             <v-card-text>Time: {{item.start}}-{{item.end}}</v-card-text>
                                         </v-list-item>
                                        <v-list-item>
                                            <v-icon>home</v-icon>
                                            <v-card-text>Venue: {{item.venue}}</v-card-text>
                                        </v-list-item>
                                    </v-list-item-content>
                                </v-card>
                            </v-tab-item>
                            <v-tab-item>
                                <v-card flat>
                                    <v-list-item-content  v-for="item in timetable">
                                        <v-list-item>
                                            <div class="title">{{item.unit.name}}</div>
                                        </v-list-item>
                                         <v-list-item>
                                             <v-icon>access_time</v-icon>
                                             <v-card-text>Time: {{item.start}}-{{item.end}}</v-card-text>
                                         </v-list-item>
                                        <v-list-item>
                                            <v-icon>home</v-icon>
                                            <v-card-text>Venue: {{item.venue}}</v-card-text>
                                        </v-list-item>
                                    </v-list-item-content>
                                </v-card>
                            </v-tab-item>
                        </v-tabs>
                    </v-card>
                </v-flex>
        </v-layout>
        <v-layout wrap pb-2>
            <v-flex xs12 md8>
                <v-card flat>
                    <v-card-text><div class="title">My Plate</div></v-card-text>
                    <v-simple-table>
                        <thead>
                        <tr>
                            <th>Type</th>
                            <th>Lecturer</th>
                            <th>Unit</th>
                            <th>Due Date</th>
                        </tr>

                        </thead>
                        <tbody>
                            <tr v-for="item in upcoming">
                                <td><v-chip :class="`${item.type} white--text my-my2 caption` ">{{item.type}}</v-chip></td>
                                <td><v-avatar size="30" pl-2><v-img :src="item.lec.avatar"/></v-avatar><v-card-text>{{item.lec.title}} {{item.lec.f_name}} {{item.lec.l_name}}</v-card-text></td>
                                <td>{{item.unit.name}}</td>
                                <td>{{item.due_date}}</td>
                            </tr>
                        </tbody>
                    </v-simple-table>
                </v-card>
            </v-flex>

            <v-flex pa-1 md4 xs12 pl-2>
                <v-card flat>
                    <v-card-text><div class="title">Notice Board</div></v-card-text>
                    <v-simple-table>
                        <thead>
                        <tr>
                            <th class="text-left">Announcement</th>
                            <th class="text-left">Date Posted</th>

                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="notice in nb_info">
                            <td>{{notice.text}}</td>
                            <td><div class="right"><v-chip small color="red" dark>{{notice.date_posted}}</v-chip></div></td>

                        </tr>
                        </tbody>
                    </v-simple-table>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
    import Todo from './Todo'
    import axios from 'axios'
    export default {
        name: 'Home',
        components: {
            Todo,
        },
        data() {
            return {
                msg: 'Welcome home',
                profileInfo: null,
                nb_info: null,
                timetable: null,
                upcoming: null,
                breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/#/Home',
                    },
                    {
                        text: 'Dashboard',
                        disabled: true,
                        href: 'breadcrumbs_dashboard',
                    },
                ]
            }
        },
        methods: {
            getProfile() {
                var p = this;
                axios
                    .get('/students/profile/')
                    .then(response => (
                        p.profileInfo = response.data))
                    .catch(error => console.log(error))
            },
            getNotices() {
                var p = this;
                axios
                    .get('notifications/')
                    .then(response => (
                        p.nb_info = response.data
                    ))
                    .catch(error => console.log(error))
            },

            getMonSchedule(){
               const p = this;
               let url = 'timetable/?';
               const d = 'Monday';
               if(d){
                   const x = d;
                   url = `${url}&day=${x}`;
               }
               axios
                   .get(url)
                   .then(response=>(
                       p.timetable = response.data
                   ))
                   .catch(error=>(console.log(error)))

           },
            getTueSchedule(){
                const p = this;
               let url = 'timetable/?';
               const d = 'Tuesday';
               if(d){
                   const x = d;
                   url = `${url}&day=${x}`;
               }
               axios
                   .get(url)
                   .then(response=>(
                       p.timetable = response.data
                   ))
                   .catch(error=>(console.log(error)))
           },
            getWedSchedule(){
                 const p = this;
               let url = 'timetable/?';
               const d = 'Wednesday';
               if(d){
                   const x = d;
                   url = `${url}&day=${x}`;
               }
               axios
                   .get(url)
                   .then(response=>(
                       p.timetable = response.data
                   ))
                   .catch(error=>(console.log(error)))
           },
            getThurSchedule(){
                 const p = this;
               let url = 'timetable/?';
               const d = 'Thursday';
               if(d){
                   const x = d;
                   url = `${url}&day=${x}`;
               }
               axios
                   .get(url)
                   .then(response=>(
                       p.timetable = response.data
                   ))
                   .catch(error=>(console.log(error)))
           },
            getFriSchedule(){
                 const p = this;
               let url = 'timetable/?';
               const d = 'Friday';
               if(d){
                   const x = d;
                   url = `${url}&day=${x}`;
               }
               axios
                   .get(url)
                   .then(response=>(
                       p.timetable = response.data
                   ))
                   .catch(error=>(console.log(error)))
           },

            getUpcoming(){
                const p = this;
                axios
                    .get('academics/myplate/')
                    .then(response=>(
                        p.upcoming = response.data
                    ))
                    .catch(error=>console.log(error))
            }
        },
        created() {
            this.getProfile();
            this.getNotices();
            this.getUpcoming();
        }
    }
</script>
<style scoped lang="scss">
    .v-chip.CAT{
        background: #FFC107
    }

    .v-chip.Assignment{
        background: #8BC34A
    }
</style>