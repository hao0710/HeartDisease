<template>
  <div>
    <canvas id="planet-chart"></canvas>
  </div>
</template>

<script>
import planetChartData from '../../chart-data.js';

export default {
  name: 'SampleChart',
  data() {
    return {
      planetChartData: planetChartData,
    };
  },
  methods: {
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
      });
    },
  },
  mounted() {
    this.createChart('planet-chart', this.planetChartData);
  },
};
</script>

<style scoped>
</style>
