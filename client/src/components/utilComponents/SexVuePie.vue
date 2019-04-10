<template>
  <div class="vue-chartjs">
    <my-pie-chart :data="data" :options="options"/>
  </div>
</template>

<script>
import MyPieChart from '@/components/utilComponents/MyPieChart';
import { data, options } from './SexChart.js';

export default {
  name: 'VueScaterjs',
  components: {
    MyPieChart,
  },
  data() {
    return {
      data,
      options,
    };
  },
};
</script>

<style scoped>

</style>

