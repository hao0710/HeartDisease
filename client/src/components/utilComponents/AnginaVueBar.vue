<template>
  <div class="vue-chartjs">
    <my-bar-chart :data="data" :options="options"/>
  </div>
</template>

<script>
import MyBarChart from '@/components/utilComponents/MyBarChart';
import { data, options } from './AnginaChart';

export default {
  name: 'VueScaterjs',
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

