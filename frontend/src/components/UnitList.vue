
<template>
  <div id="unitlist">
    <h2>This is the unit detail Component</h2>
<!--  <ul v-for="unit in unitList">-->
<!--    <li>{{unit.id}}</li>-->
<!--    <li id="detail" @click="getUnitDetail()" v-model="unitList">{{unit.unit.unit.name}}</li>-->
<!--  </ul>-->
  <section v-for="unit in unitList">
    <h3>{{unit.unit.unit.name}}</h3>
    <router-link :to="'/Units/'+ unit.id" class="btn btn-primary">Read more..</router-link>
  </section>
  </div>
</template>
<script>
import {EventBus} from "../main";

export default {
    data() {
      return{
        unitList: null,
        unitDetail: null
      }
    },
    methods: {
      getUnitList() {
        var p = this;
        axios
          .get('/academics/units/')
          .then(response => (
            p.unitList = response.data
          ))
          .catch(error => (console.log(error)));
        EventBus.$emit('getUnitList', p.unitList);

      },

      // getUnitDetail() {
      //   this.$router.push({name: 'UnitDetail'});
      // },
    },
    created() {
      this.getUnitList();
    }
  }
</script>
<style scoped>
  #detail{
    cursor: pointer;
  }
</style>
