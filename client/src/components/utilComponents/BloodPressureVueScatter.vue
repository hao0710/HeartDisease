<template>
  <div class="vue-chartjs">
    <my-scatter-chart :data="data" :options="options"/>
  </div>
</template>

<script>
import MyScatterChart from '@/components/utilComponents/MyScatterChart';
import { data, options } from './BloodPressureChart';

export default {
  name: 'VueScaterjs',
  components: {
    MyScatterChart,
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

