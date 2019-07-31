<template>
    <div id="Navigation">
      <nav class="navbar navbar-expand-lg navbar-dark fixed-top navbar-default bg-dark">
        <div class="container">
                <a class="navbar-brand" href="/">
                    <img class="img-fluid" src="/static/dist/assets/img/logo.png" alt="School Portal">
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                       <li class="nav-item">
                         <router-link class="nav-link" :to="{name: 'Home'}">
                              Home
                            </router-link>
                       </li>
                      <li class="nav-item">
                         <router-link class="nav-link" :to="{name: 'Academics'}">
                              Academics
                            </router-link>
                       </li>
                      <li class="nav-item">
                         <router-link class="nav-link" :to="{name: 'Finance'}">
                              Finances
                            </router-link>
                       </li>
                    </ul>
                    <ul class="navbar-nav my-2 my-lg-0">

                        <li class="nav-item">
                          <template v-if="loggedIn">
                            <a id='logout' class="nav-link" @click="logout">Logout</a>
                          </template>
                          <template v-else>
                            <router-link class="nav-link" :to="{name: 'Login'}">
                              Login
                            </router-link>
                          </template>
                        </li>
                    </ul>
                </div>
        </div>
      </nav>
    </div>
</template>

<script>
    export default {
        name: "Navigation",
        data(){
            return {
              loggedIn: 0
            }
        },

        methods:{
          logout(){
            localStorage.removeItem("token");
            this.loggedIn = 0;
            window.location.href = "/";
          }
        },
        created(){
          var token = localStorage.getItem('token');
          if (token) {
           this.loggedIn = 1;
          }
        }
    }
</script>

<style scoped>
  #logout{
    cursor: pointer;
  }

</style>
