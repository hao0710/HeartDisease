<template>
  <div>
    <!--<Carousel></Carousel>-->
    <!--<Navbar></Navbar>-->
    <hr>
    <hr>
    <div>
      <b-jumbotron
        header="Heart Disease Analysis"
        lead="Predict heart disease using machine learning"
      >
        <b-button variant="primary" href="#/predict">Predict</b-button>
      </b-jumbotron>
    </div>
    <div class="row">
      <div class="col-md-6">
        <div class="tile">
          <div class="container">
            <CardModels></CardModels>
          </div>
        </div>
      </div>
    </div>

    <!-- <p>{{ msg }}</p>
    <router-link to="/stats">Go to stats</router-link>
    <router-view/> -->
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      msg: "I am the home component"
    };
  }
};
</script>

<style scoped>
h1,
h2 {
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
  position: middle;
  background: rgb(248, 248, 248);
  border-radius: 3px;
  padding: 20px;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12),
    0 3px 1px -2px rgba(0, 0, 0, 0.2);
  margin-bottom: 30px;
  transition: all 0.3s ease-in-out;
  text-align: left;
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin-left: auto;
  margin-right: auto;
  align-items: center;
  justify-content: center;
}
</style>
