<style></style>
<template>
  <div id="home">
    <h2>{{msg}}</h2>
    <h3>{{nb_info}}</h3>
    <thead>
    <tr>
      <th>Text</th>
      <th>Date</th>
      <th>Time</th>
    </tr>
    </thead>
    <template v-for="i in nb_info">
     <tr>
       <td>{{i.text}}</td>
       <td>{{i.date_posted}}</td>
       <td>{{i.time_posted}}</td>
     </tr>

   </template>
    <div class="todos">
      <todo/>
    </div>
  </div>
</template>
<script>
 import Todo from './Todo.vue';
 // import 'bootstrap/dist/css/bootstrap.min.css'
  export default {
      name: 'Home',
    components:{
      Todo,
    },
    data () {
      return {
          msg: 'Welcome home',
          profileInfo: null ,
          nb_info: null,
      }
    },
    methods : {
      getProfile(){
        var  p = this;
        axios
          .get('/students/profile/')
          .then(response => (
            p.profileInfo=response.data))
          .catch(error =>console.log(error))
      },

      getNotices(){
        var p = this;
      axios
        .get('notifications/')
        .then(response => (
          p.nb_info =response.data
        ))
        .catch(error => console.log(error))
      },
    },

    created(){
        this.getProfile();
        this.getNotices();
        console.log("im here now");
      }

  }
</script>
