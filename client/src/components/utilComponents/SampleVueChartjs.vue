<template>
  <div class="vue-chartjs">
    <my-bar-chart :data="data" :options="options"/>
  </div>
</template>

<script>
import MyBarChart from '@/components/utilComponents/MyBarChart';
import { data, options } from './chartData';

export default {
  name: 'VueChartjs',
  components: {
    MyBarChart,
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

