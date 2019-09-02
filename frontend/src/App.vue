<template>
  <div class="app">
    <v-app >
      <navigation/>
        <v-content class="grey lighten-4" >
           <router-view/>
        </v-content>
  </v-app>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import axios from 'axios';
export default {
  name: 'App',
  components: {
    Navigation,
  },
  data (){
    return{
    }
  },
  created() {
    const token = localStorage.getItem("token");
    if (token){
      axios.defaults.headers.common['Authorization'] = "Token " + token;
      this.$router.push({name: "Home"});
    }
    else{
      this.$router.push({name: "Login"});
    }
  }
};
</script>
