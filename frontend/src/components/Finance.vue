<template>
    <div id="Finance" class="container">
      <h2>Finance</h2>
      {{finance}}
      <h5>{{financeHistory}}</h5>
    </div>
</template>

<script>
    export default {
      name: "Finance",
      data(){
          return {
            finance: null,
            financeHistory: null
          }
      },

      methods: {
         getFinance(){
           var p = this;
           axios
             .get('/finance/current/')
             .then(response => (
               p.finance = response.data
             ))
             .catch(error=>(console.log(error)))
         },

         getFinanceHistory(){
           var p = this;
           axios
             .get('/finance/history/')
             .then(response =>(
               p.financeHistory = response.data
             ))
             .catch(error=>(console.log(error)))
         }
      },
      created(){
          this.getFinance();
          this.getFinanceHistory();
      }
    }
</script>

<style scoped>

</style>
