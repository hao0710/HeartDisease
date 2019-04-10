<template>
  <div class="chartjs">
    <canvas :id="CHART_ID" style="position: relative; height:40vh; width:40vw"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js';
import { data, options } from './chartData';
const CHART_ID = 'my-chart';

export default {
  name: 'Chartjs',
  data() {
    return {
      CHART_ID,
    };
  },
  mounted() {
    const ctx = document.getElementById('my-chart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data,
      options,
    });
  },
};
</script>