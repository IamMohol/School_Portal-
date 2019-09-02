import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'


import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import vuetify from './plugins/vuetify';
import DaySpanVuetify from 'dayspan-vuetify'
import 'dayspan-vuetify/dist/lib/dayspan-vuetify.min.css'
import 'dayspan-vuetify/dist/lib/dayspan-vuetify.min'

Vue.config.productionTip = false;
Vue.use(DaySpanVuetify,{
    methods: {
        getDefaultEventColor:() => '#f05d5e'
    }
});
Vue.use(require('vue-chartist'));
Vue.use(VueRouter);
import  routes from './router/routes'
const router = new VueRouter({
    routes
});

new Vue({
  vuetify,
    router,
  render: h => h(App)
}).$mount('#app');
