<template>
  <div id="todo">
    <h2>{{msg}}</h2>
    <h3>{{todo}}</h3>
  </div>
</template>
<script>
  export  default {
    name: 'Todo',
    data() {
      return {
        msg:"Welcome to the Todo's Component",
        todo: null
      }
    },
    methods:{
      listTodos(){
        var p = this;
        axios
          .get('todos/')
          .then(response=>(
            p.todo = response.data
          ))
          .catch(error => console.log(error))
      },
      postTodos (){
        var p = this;
        var url = '/todos/?';
        if(this.id){
          var x = this.id;
          url = `${url}id=${x}`;
        }

        axios
        .post(url)
          .then(response=>(
            p.todo =response.data
          ))
          .catch(error=>console.log(error))
      },

      deleteTodo(){
        var p = this;
        var url = '/todos/?';
        if (this.id){
          var x = this.id;
          url = `${url}id=${x}`
        }
        axios
          .delete(url)
          .then(response=>(
            p.todo = response.data
          ))
          .catch(error=>console.log(error))
      }
    },
    created() {
      this.listTodos();
    }
  }
</script>
<style></style>

