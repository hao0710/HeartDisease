<template>
  <div>
    <!--<Carousel></Carousel>-->
    <!--<Navbar></Navbar>-->
  <div class="row">
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Planet Line</h3>
              <SampleChart></SampleChart>
          </div>
      </div>
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Planet Pie</h3>
              <SampleChart1></SampleChart1>
          </div>
      </div>
  </div>
  <div class="row">
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Color Vote by Chartjs</h3>
              <SampleChartjs></SampleChartjs>
          </div>
      </div>
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Color Vote by VueChartjs</h3>
              <SampleVueChartjs></SampleVueChartjs>
          </div>
      </div>
  </div>
  <div class="row">
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Npm Stats</h3>
              <Requestdata></Requestdata>
          </div>
      </div>
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Resting Blood Pressure</h3>
              <SampleVueScatter></SampleVueScatter>
          </div>
      </div>
  </div>
    <p>{{ msg }}</p>
    <router-link to="/stats">Go to stats</router-link>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'Planet',
  data() {
    return {
      msg: 'I am the planet component',
    };
  },
};
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.tile {
    position: relative;
    background: #ffffff;
    border-radius: 3px;
    padding: 20px;
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
    margin-bottom: 30px;
    transition: all 0.3s ease-in-out;
}

.row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
}

</style>
