<template>
  <div id="app">
    <navigation />
    <router-view/>
    <div id="footer" class="container">
      Footer
    </div>
  </div>
</template>

<script>
  import Navigation from "./components/Navigation.vue";

export default {
  name: 'app',
  components: {
    Navigation
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created(){
    var token = localStorage.getItem("token");
    if (token){
      axios.defaults.headers.common['Authorization'] = "Token " + token;
      this.$router.push({name: "Home"});
    }
    else{
      this.$router.push({name: "Login"});
    }
  }
}
</script>

<style scoped lang="scss">
  #app{
    padding-top: 70px;
    padding-bottom: 20px;
  }
  #footer{
    position: fixed;
    bottom: 0px;
    left: 0px;
    right: 0px;
    border-top: 1px solid #eee;
    padding-top: 10px;
    padding-bottom: 10px;
  }
</style>
