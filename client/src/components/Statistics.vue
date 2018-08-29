<template>
  <container>
    <h2 class="text-center m-4" >Статистика правопорушень за 2018 рік</h2>
    <commit-chart :chartData="monthData" :options="commitOptions" :height="100"></commit-chart>
    <pie-chart :chartData="networkData" :options="networkOptions" :height="100"></pie-chart>
    <pie-chart :chartData="peopleData" :options="peopleOptions" :height="100"></pie-chart>
  </container>
</template>

<script>
import axios from 'axios';
import CommitChart from './CommitChart';
import LineChart from './LineChart';
import PieChart from './PieChart';

export default {
  name: 'Statistics',
  components: {
    'commit-chart': CommitChart,
    'line-chart': LineChart,
    'pie-chart': PieChart,
  },
  data() {
    return {
      networkData: null,
      monthData: null,
      violations: [],
      peopleData: null,
      networkOptions: {
        title: {
          display: true,
          text: 'Pie chart by network',
          fontSize: 25,
        },
      },
      peopleOptions: {
        title: {
          display: true,
          text: 'Pie chart by violations founders',
          fontSize: 25,
        },
      },
      commitOptions: {
        title: {
          display: true,
          text: 'Line chart by month',
          fontSize: 25,
        },
        legend: {
          display: false,
        },
        responsive: true,
        lineTension: 1,
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true,
              padding: 25,
            },
          }],
        },
      },
    };
  },
  mounted() {
    this.getViolations();
  },
  methods: {
    getViolations() {
      const path = 'http://192.168.0.104:5000/violations';
      axios.get(path)
        .then((response) => {
          this.violations = response.data.data;
          this.getViolData(this.violations);
        });
    },
    getViolData(viol) {
      let i;
      let k;
      let month = [];
      let violMonth = [0,0,0,0,0,0,0,0,0,0,0,0];
      let monthCount = [0,0];
      for (i = 1; i < 12; i += 1) {
        for (k = 0; k < viol.length; k += 1) {
          month = parseInt(viol[k]['date'].split('.')[1], 10);
          if (month === i) {
            violMonth[i-1] += 1;
          }
        }
      }
      this.monthData = {
        labels: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
          'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'],
        datasets: [
          {
            label: 'Кількість порушень',
            backgroundColor: [
              'rgba(255, 99, 132, 0.8)',
              'rgba(54, 162, 235, 0.8)',
              'rgba(255, 206, 86, 0.8)',
              'rgba(75, 192, 192, 0.8)',
              'rgba(153, 102, 255, 0.8)',
              'rgba(79, 110, 0, 0.8)',
              'rgba(235, 219, 0, 0.8)',
              'rgba(212, 134, 0, 0.8)',
              'rgba(252, 93, 0, 0.8)',
              'rgba(64, 118, 255, 0.8)',
              'rgba(44, 33, 255, 0.8)',
              'rgba(140, 0, 14, 0.8)',
              ],
            borderWidth:1,
            borderColor: '#777',
            hoverBorderWidth:3,
            hoverBorderColor: '#000',
            data: [violMonth[0],violMonth[1],violMonth[2],violMonth[3],violMonth[4],violMonth[5],
            violMonth[6],violMonth[7],violMonth[8],violMonth[9],violMonth[10],violMonth[11]],
          },
        ],
      };
      for (k = 0; k < viol.length; k += 1) {
        if (viol[k]['network'] === 'АСУ-дніпро') {
          monthCount[0] += 1;
        }
        if (viol[k]['network'] === 'ІСД-інтернет') {
          monthCount[1] += 1;
        }
      }
      this.networkData = {
        labels: ['АСУ-дніпро', 'ІСД-інтернет'],
        datasets: [
          {
            label: 'Network',
            backgroundColor: ['rgba(26, 56, 255, 0.8)', 'rgba(235, 219, 0, 0.8)'],
            data: [monthCount[0], monthCount[1]],
            borderWidth: 3,
            hoverBorderWidth:3,
            hoverBorderColor: '#000',
          },
        ],
      };
    },
  },
};
</script>

<style scoped>

</style>
