<template>
  <div id="unitDetail">
    {{unitList}}
  </div>
</template>
<script>
  import {EventBus} from "../main";

  export default {
    data(){
      return{
          unitList: null
      }
    },

    methods:{
      getUnitDetail(){
        var p = this;
        var url= 'academics/units/?';

        if (this.$route.params.id){
          var x = this.$route.params.id;
          url = `${url}&id=${x}`;
        }
        axios
          .get(url)
          .then(response=>(
            p.unitList= response.data
          ))
          .catch(error=>(console.log(error)))
      }
    },

    created() {
      this.getUnitDetail();

    },
  }
</script>
<style></style>
