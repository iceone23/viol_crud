<template>
  <div>
    <h2 class="text-center m-4" >Статистика правопорушень за 2018 рік</h2>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Statistics',
  data() {
    return {
      violations: [],
      viol_count: [],
      month_count: [],
      networkData: [
        ['ІСД-інтернет', 'АСУ-дніпро'],
        ['ІСД-інтернет', 5],
        ['АСУ-дніпро', 10],
      ],
      networkOptions: {
        title: 'Правопорушення по мережам',
      },
      monthData: [
        ['Month', 'Кількість порушень'],
        ['січень', 1],
        ['лютий', 2],
        ['березень', 3],
        ['квітень', 4],
        ['травень', 5],
        ['червень', 6],
        ['липень', 7],
        ['серпень', 8],
        ['вересень', 9],
        ['жовтень', 10],
        ['листопад', 11],
        ['грудень', 12],
      ],
      monthOptions: {
        title: 'Виявлені правопорушення по місяцям',
      },
      peopleData: [
        ['ПІБ', 'Кількість виявлених порушень'],
        ['п/п-к Неграш В.М.', 10],
        ['м-р Вишневський С.М.', 7],
        ['ст.л-нт Моторний О.В.', 4],
        ['л-нт Крушевницька', 2],
      ],
      peopleOptions: {
        title: 'Кількість правопорушень людьми',
      },
    };
  },
  mounted() {
    this.getViolations();
    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'GitHub Commits',
          backgroundColor: '#f87979',
          data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11],
        },
      ],
    });
  },
  methods: {
    getViolations() {
      const path = 'http://192.168.0.104:5000/violations';
      axios.get(path)
        .then((response) => {
          this.violations = response.data.data;
        });
    },
    getViolCount(viol) {
      let i;
      let k;
      let month = [];
      for (i = 1; i < 12; i += 1) {
        for (k = 0; k < viol.length; k += 1) {
          //get month from date string
          month = parseInt(viol[k]['date'].split('.')[1], 10);
          console.log(month);
          if (month == i) {
            this.viol_count[i] += 1;
          }
        }
      }
      for (i = 0; i < 12; i += 1) {
        console.log(this.viol_count[i]);
      }
    },
    getNetworkData(viol) {
      let k;
      for (k = 0; k < viol.length; k += 1) {
        if (viol[k]['network'] == 'АСУ-дніпро') {
          this.month_count[0] += 1;
        }
        if (viol[k]['network'] == 'ІСД-інтернет') {
          this.month_count[1] += 1;
        }
      }
    },
  },
};
</script>

<style scoped>

</style>
