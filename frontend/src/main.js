import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);
import routes from './router/routes.js'
const router = new VueRouter({
  routes
});
export const EventBus = new Vue();
new Vue({
  el: '#app',
  router,
  render: h => h(App)
});

