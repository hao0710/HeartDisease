<template>
  <div>
    <canvas id="planet-chart1" style="position: relative; height:40vh; width:40vw"></canvas>
  </div>
</template>

<script>
import planetChartData from '../../chart-data1.js';

export default {
  name: 'SampleChart1',
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
    this.createChart('planet-chart1', this.planetChartData);
  },
};
</script>

<style scoped>

</style>
