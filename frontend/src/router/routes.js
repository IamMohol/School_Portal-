import Login from '../components/Login.vue'
import Academics from '../components/Academics.vue'
import Finance from '../components/Finance.vue'
import Home from '../components/Home.vue'
import Todo from '../components/Todo.vue'
import UnitList from '../components/UnitList'
import  UnitDetail from '../components/UnitDetail'


const routes = [
  { path: '/', component: Home, name:"Home"},
  { path: '/Login', component:Login, name:"Login"},
  { path: '/Academics', component: Academics, name:"Academics"},
  { path: '/Finance', component: Finance, name:"Finance"},
  { path: '/Home', component: Home, name:"Home"},
  { path: '/Todo', component: Todo, name:"Todo"},
  { path: '/Units', component: UnitList, name:"UnitList"},
  { path: '/Units/:id', component: UnitDetail, name:"UnitDetail"},
];
export default routes;
