
<style> </style>
<template>
  <div id="Login">
    <v-card width="500" class="mx-auto mt-7 pt-lg-10">
      <v-card-title>
        <h1>Login</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
                  label="Username"
                  v-model="username"
                  prepend-icon="account_circle"
          />
          <v-text-field
                  label="Password"
                  :type="showPassword ? 'text' : 'password'"
                  v-model="password"
                  prepend-icon="lock"
                  :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                  @click:append="showPassword = !showPassword"
          />
        </v-form>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="primary"  @click="login">Login</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>
<script>
    import  axios from 'axios'
  export default {
    data: function() {
      return{
        username: null,
        password: null,
        showPassword: false
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