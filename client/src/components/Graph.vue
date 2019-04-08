<template>
  <div>
    <!--<Carousel></Carousel>-->
    <!--<Navbar></Navbar>-->
  <hr>
  <hr>
  <b-jumbotron header="visualize the statistics for basic information" lead="by groups of
age and sex">
  </b-jumbotron>
  <div class="row">
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Resting Blood Pressure</h3>
              <BloodPressureVueScatter></BloodPressureVueScatter>
          </div>
      </div>
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Serum Cholestoral in mg/dl</h3>
              <CholestoralVueScatter></CholestoralVueScatter>
          </div>
      </div>
  </div>

  <div class="row">
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Maximum Heart Rate Achieved</h3>
              <HeartRateVueScatter></HeartRateVueScatter>
          </div>
      </div>
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Oldpeak</h3>
              <OldpeakVueScatter></OldpeakVueScatter>
          </div>
      </div>
  </div>

  <div class="row">
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Chest Pain Type</h3>
              <ChestPainVueBar></ChestPainVueBar>
          </div>
      </div>
      <div class="col-md-6">
          <div class="tile">
              <h3 class="tile-title">Oldpeak</h3>
              <OldpeakVueScatter></OldpeakVueScatter>
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
  name: 'Home',
  data() {
    return {
      msg: 'I am the home component',
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
/*{
  color: #42b983;
}*/

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
