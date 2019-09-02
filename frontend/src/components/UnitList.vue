<template>
    <div id="unitlist">
        <v-container>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-icon>class</v-icon>
                        <v-card-text><div class="title">Courses Registered</div></v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>

            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-breadcrumbs :items="breadcrumb" divider=">"/>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row pb-2>
                <v-flex xs12 md12 pb-4 v-for="i in unitList" :key="i.id">
                    <v-card flat  pb-4>
                        <v-img
                            class="white--text"
                            height="200px"
                            :src="i.unit.thumbnail"
                        >
                            <v-card-title class="align-end fill-height">{{i.unit.unit.code}} {{i.unit.unit.name}}</v-card-title>
                        </v-img>
                        <v-list-item-content>
                            <v-list-item>
                                <v-avatar><v-img :src="i.unit.lecturer.avatar"></v-img></v-avatar>
                                <v-card-text>{{i.unit.lecturer.title}}  {{i.unit.lecturer.f_name}}  {{i.unit.lecturer.l_name}}</v-card-text>
                            </v-list-item>
                            <v-list-item>
                                <v-icon>perm_identity</v-icon>
                                <v-card-text>{{i.unit.lecturer.email}}</v-card-text>
                                <v-spacer/>
                                <v-icon>local_phone</v-icon>
                                <v-card-text>{{i.unit.lecturer.phone}}</v-card-text>
                            </v-list-item>
                            <v-card-actions>
                                <v-btn
                                        outlined
                                        color="#3b60e4"
                                        :to="'/Units/'+ i.id"
                                >
                                    Explore
                                </v-btn>
                            </v-card-actions>
                        </v-list-item-content>
                    </v-card>

                </v-flex>

            </v-layout>
        </v-container>
<!--      <v-flex>-->
<!--                    <v-card flat>-->
<!--                        <v-card-text class="title">Courses Registered</v-card-text>-->
<!--                        <v-divider></v-divider>-->

<!--                        <v-flex xs12 md12 pl-5 pb-3 v-for="unit in unitList" :key="unit.id">-->
<!--                             <v-card  pl-10 pb-4 row >-->

<!--                            &lt;!&ndash;    class="mx-auto"&ndash;&gt;-->

<!--                            <v-img-->
<!--                                    class="white&#45;&#45;text"-->
<!--                                    height="200px"-->
<!--                                    :src="unit.unit.thumbnail"-->
<!--                            >-->
<!--                                <v-card-title class="align-end fill-height">{{unit.unit.unit.code}} - {{unit.unit.unit.name}}</v-card-title>-->
<!--                            </v-img>-->

<!--                            <v-card-text>-->
<!--                                <span>Lecturer:</span><br>-->
<!--                                <span class="text&#45;&#45;primary">-->
<!--                                    <v-avatar><v-img :src="unit.unit.lecturer.avatar"></v-img></v-avatar>-->
<!--                                    <span pl-2>{{unit.unit.lecturer.title}} {{unit.unit.lecturer.f_name}} {{unit.unit.lecturer.l_name}}</span><br>-->
<!--                                    <v-icon> perm_identity</v-icon>-->
<!--                                    <span pl-2>{{unit.unit.lecturer.email}}</span><br>-->
<!--                                    <v-icon>local_phone</v-icon>-->
<!--                                    <span pl-2>{{unit.unit.lecturer.phone}}</span>-->
<!--                                </span>-->
<!--                            </v-card-text>-->

<!--                            <v-card-actions>-->
<!--                                <v-btn-->
<!--                                        text-->
<!--                                        color="orange"-->
<!--                                        :to="'/Units/'+ unit.id"-->
<!--                                >-->
<!--                                    Explore-->
<!--                                </v-btn>-->
<!--&lt;!&ndash;                                <v-btn&ndash;&gt;-->
<!--&lt;!&ndash;                                        text&ndash;&gt;-->
<!--&lt;!&ndash;                                        color="orange"&ndash;&gt;-->
<!--&lt;!&ndash;                                >&ndash;&gt;-->
<!--&lt;!&ndash;                                    Explore&ndash;&gt;-->
<!--&lt;!&ndash;                                </v-btn>&ndash;&gt;-->
<!--                            </v-card-actions>-->
<!--                        </v-card>-->
<!--                        </v-flex>-->

<!--                    </v-card>-->
<!--                </v-flex>-->
    </div>

</template>
<script>
    import axios from 'axios'
   export default {
    data() {
      return{
        unitList: null,
        unitDetail: null,
          breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/',
                    },
                    {
                        text: 'Course',
                        disabled: true,
                        href: '/#/Units',
                    },
                ],
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
        // EventBus.$emit('getUnitList', p.unitList);
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
<style></style>
