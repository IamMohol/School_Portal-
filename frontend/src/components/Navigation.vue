<template>
    <div>
        <template v-if="loggedIn">
            <v-navigation-drawer
                    v-model="drawer"
                    expand-on-hover
                    app
                    color="#080708"
                    dark>
                <v-list dense nav class="py-0" v-for="i in profileInfo">
                    <v-list-item two-line>
                        <v-list-item-avatar>
                            <v-img :src="i.avatar"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title>{{i.first_name}} <span>{{i.l_name}}</span></v-list-item-title>
                            <v-list-item-subtitle>{{i.registration_number}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-divider/>

                    <v-list-item link :to="{path:'/'}">
                        <v-list-item-icon>
                            <v-icon>dashboard</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-content>Home</v-list-item-content>
                        </v-list-item-content>
                    </v-list-item>

<!--                    <v-list-item link :to="{path:'/Academics'}">-->
<!--                        <v-list-item-icon>-->
<!--                            <v-icon>school</v-icon>-->
<!--                        </v-list-item-icon>-->
<!--                        <v-list-item-content>-->
<!--                            <v-list-item-content>Academics</v-list-item-content>-->
<!--                        </v-list-item-content>-->
<!--                    </v-list-item>-->
                    <v-list-item link :to="{path:'/Units'}">
                        <v-list-item-icon>
                            <v-icon>event_note</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-content>Courses</v-list-item-content>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item link :to="{path:'/Grades'}">
                        <v-list-item-icon>
                            <v-icon>poll</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-content>Grades</v-list-item-content>
                        </v-list-item-content>
                    </v-list-item>

                    <v-list-item link :to="{path:'/Finance'}">
                        <v-list-item-icon>
                            <v-icon>account_balance</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-content>Finance</v-list-item-content>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item link :to="{path:'/Timetable2'}">
                        <v-list-item-icon>
                            <v-icon>calendar_today</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-content>Timetable</v-list-item-content>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-navigation-drawer>
        </template>

        <v-app-bar
                color="#3b60e4"
                dense
                dark
                app
                clipped-right
        >
            <template v-if="loggedIn">
                <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            </template>


            <v-toolbar-title>School Portal</v-toolbar-title>

            <v-spacer></v-spacer>
            <template v-if="loggedIn">
                <v-btn icon @click="logout">
                    <v-icon>exit_to_app</v-icon>
                </v-btn>
            </template>
        </v-app-bar>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Navigation",
        data() {
            return {
                loggedIn: 0,
                drawer: true,
                profileInfo: null
            }
        },
        methods: {
            logout() {
                localStorage.removeItem("token");
                this.loggedIn = 0;
                window.location.href = "/";
            },

            getProfile() {
                var p = this;
                axios
                    .get('/students/profile/')
                    .then(response => (
                        p.profileInfo = response.data))
                    .catch(error => console.log(error))
            },
        },
        created() {
            var token = localStorage.getItem('token');
            if (token) {
                this.loggedIn = 1;
            }
            this.getProfile();
        }
    }
</script>

<style scoped>
    #logout {
        cursor: pointer;
    }
</style>yle>