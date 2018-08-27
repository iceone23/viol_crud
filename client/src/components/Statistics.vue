<template>
  <div>
    <div class="class11">
      <li v-for="violation in violations"> {{ violation.date}} </li>
    </div>
    <div class="color">
      <h2>Мережа</h2>
    </div>
<!--
    <p>{{ getDepartment() }}</p>
-->
    <chartjs-doughnut :labels="labels" :datasets="datasets" :option="option">
      <canvas :method="getDepartment" v-if="!target" ref="canvas" :width="width" :height="height" ></canvas></chartjs-doughnut>
    <br>
    <div>
      <div class="color">
        <h2>Виявник</h2>
      </div>
      <chartjs-bar :datasets="datasets1"
                   :labels="labels1"
                   :option="option1"
                   :beginzero="true">
      </chartjs-bar>
      <br>
    </div>
    <div>
      <div class="color">
        <h2>Підпорядкування</h2>
      </div>
      <chartjs-polar-area :datasets="dataarea" :labels="mylabels" :scalesdisplay="false">
      </chartjs-polar-area>
    </div><br>
    <div class="dashboard" >
      <div class="color">
        <h2>Періодичність</h2>
      </div>
      <chartjs-line :beginzero="true"
                    :labels="labelsLine"
                    :datasets="mydatasets"
      >
      </chartjs-line>
      <br>
    </div>
    <!--<b-modal

    {{ this.violations }}

      id="deleteModal"
      ref="deleteModal"
      @ok="removeViolation"
      size="md"
      title="Видалення запису"
      header-bg-variant="dark"
      header-text-variant="light"
      body-bg-variant="light"
      body-text-variant="dark"
      footer-bg-variant="dark"
      footer-text-variant="light">
      <b-container>
        <b-row class="mb-4 text-center">
          <h2>Ви дійсно бажаєте видалити запис № {{ row.value}}</h2>
        </b-row>
      </b-container>
    </b-modal>-->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Statistics',
  data () {
    return {
      violations: [],
      labels: ['Інтернет', 'Дніпро'],
      datasets: [
        {
          data: [30, 70],
          backgroundColor: ['#A3A1FB', '#A1FBE6']
        }
      ],
      labels1: ['л-т Крушеницька', 'л-т Унтілова', 'м-р Беспалов', ''],
      datasets1: [
        {
          label: 'Виявник',
          data: [30, 50, 80, 0],
          backgroundColor: ['#A3A1FB', '#A1FBE6', '#CBFBA1']
        }
      ],
      mylabels: ['СВ', 'ВМС', 'ССО', 'ДШВ', 'ПС'],
      dataarea: [
        {
          data: [80, 40, 60, 20, 10],
          backgroundColor: ['#A3A1FB', '#5EE2A0', '#FF6565', '#FEC163', '#F9E140']
        }
      ],
      labelsLine: ['January', 'February', 'March', 'April', 'May'],
      mydatasets: [{
        label: 'Місяць',
        fill: true,
        data: [65, 59, 80, 81, 56],
        backgroundColor: 'rgba(75,192,192,0.6)'
      },
        {
          label: 'Рік',
          fill: true,
          data: [15, 25, 40, 91, 106],
          backgroundColor: 'rgba(203, 251, 161,0.6)'
        },
        {
          label: '6 місяців',
          fill: true,
          data: [30, 15, 100, 29, 69],
          backgroundColor: 'rgba(161, 251, 230,0.6)'
        }],
      option: {
        title: {
          display: true,
          position: 'bottom',
          text: 'test'
        }
      },
      option1: {
        label: {
          position: 'bottom'
        }
      },
    }
  },
  methods: {
    getViolations() {
      const path = 'http://192.168.0.104:5000/violations';
      axios.get(path)
        .then((response) => {
          this.violations = response.data.data;
          console.log(this.violations);
        });
    },
   /* getDepartment () {
      let a = 0;
      let b = 0;
      let ab = {};

      if (this.violations.network == "АСУ-Дніпро") {
        a = a + 1;
      }
      ab[0] = 5;
      ab[1] = 10;
      console.log(ab);
      return ab;
    }*/
  },
  created() {
    this.getViolations();
  },
};
</script>

<style scoped>
  h2 {
    text-shadow:1px 1px 0 rgb(126,70,190),2px 2px 0 rgb(95,53,143),3px 3px 0 rgb(63,35,95),4px 4px 0 rgb(32,18,48),5px 5px 1px rgba(0,0,0,1);
    -webkit-text-shadow:1px 1px 0 rgb(126,70,190),2px 2px 0 rgb(95,53,143),3px 3px 0 rgb(63,35,95),4px 4px 0 rgb(32,18,48),5px 5px 1px rgba(0,0,0,1);
    -moz-text-shadow:1px 1px 0 rgb(126,70,190),2px 2px 0 rgb(95,53,143),3px 3px 0 rgb(63,35,95),4px 4px 0 rgb(32,18,48),5px 5px 1px rgba(0,0,0,1);
    color:#9e58ee;
    font-size:47px;
    font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif;
  }
  .color{
    background-color: #FFF49E;
  }
</style>
