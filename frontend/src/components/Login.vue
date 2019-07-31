<style> </style>
<template>
  <div id="Login">
    <div class="container">
      <form>
        <div class="form-group">
          <div class="col">
          <label for="">Username</label>
          </div>

          <div class="col">
            <input type="text" v-model="username">
          </div>
        </div>

        <div class="form-group">
          <div class="col">
          <label for="">Password</label>
          </div>

          <div class="col">
            <input type="password" v-model="password">
          </div>
        </div>

        <div class="form-group">
          <div class="col">
            <button class="btn btn-success" @click="login">Login</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>

  export default {
    data: function() {
      return{
        username: null,
        password: null,
      }
    },
    methods: {
      login() {
        var d = {
          username: this.username,
          password: this.password
        };
        var p = this;
        axios.post('/api-token-auth/', d).then(function ({data}) {
          if (data){
            localStorage.setItem('token', data.token);
            localStorage.setItem('name', data.name);
            localStorage.setItem('email', data.email);
            axios.defaults.headers.common['Authorization'] = "Token " + data.token;
            window.location.reload();
            return;
          }

          alert("Invalid credentials.");
        });
      },
    },
    created(){
    }

  }
</script>
