<template>
    <div id="Academics" class="container">
      <h2>
        Academics
      </h2>

      <div class="row" id="chooser">
        <div class="col">
          Year:
          <select class='form-control' v-model='year' name="" id="" @change="yearSemChange">
            <option value="">---</option>
            <template v-for="y in years">
              <option :value="y">{{y}}</option>
            </template>
          </select>
        </div>
        <h2>{{years}}</h2>
        <div class="col">
          Semester:
          <select class='form-control'  v-model='semester' name="" id="" @change="yearSemChange">
            <option value="">---</option>
            <template v-for="s in semesters">
              <option :value="s">{{s}}</option>
            </template>
          </select>
        </div>

        <div class="col">
          <button class="btn btn-success" @click="clear">Clear</button>
        </div>
      </div>


      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Unit</th>
            <th>Year.Sem</th>
            <th>Midterm</th>
            <th>Final</th>
<!--            <th>Grade</th>-->
          </tr>
        </thead>
        <tbody>
        <tr v-for="academic in academics" >
          <td class="col">{{academic.course_unit.unit.name}}</td>
          <td class="col">
            {{academic.course_unit.clss.year}}.{{academic.course_unit.clss.semester}}
          </td>
          <td class="col">{{academic.midterm_mark}}</td>
          <td class="col">{{academic.final_mark}}</td>
<!--          <td class="col">{{academic.grade}}</td>-->
        </tr>
        </tbody>
      </table>
<!--      <h4>{{academics}}</h4>-->
      <h6>{{year}}</h6>
    </div>
</template>

<script>
    export default {
        name: "Academics",
      data(){
          return {
            academics: null,
            years: [],
            semesters: [1, 2],
            year: "",
            semester: ""
          }
      },

      methods: {
          clear(){
            this.semester = "";
            this.year = "";
            this.getAcademics();
          },
          yearSemChange(){
            this.getAcademics();
          },
          getAcademics(){
            var p = this;
            var url = "/academics/grades/?";
            if (this.year){
              var y = this.year;
              console.log(y);
              url = `${url}year=${y}`;

              if (this.semester){
                var s = this.semester;
                url = `${url}&semester=${s}`;
              }

            }

            axios.get(url).then(function({data}){
              for(var i=0; i<data.length; i++){
                var item =data[i];
                var year = item.course_unit.clss.year;
                if (!p.years.includes(year)){
                  p.years.push(year);
                }

                var semester = item.course_unit.clss.semester;
                if (!p.semesters.includes(semester)){
                  p.semesters.push(semester);
                }
              }
              p.academics = data;
            });
          }
      },
      created(){
          this.getAcademics();
      }
    }
</script>

<style scoped>
#chooser {
  margin-bottom: 10px;
}
</style>
