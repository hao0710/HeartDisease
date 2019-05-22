<template>
<div class="wrapper">
  <div class="container">
    <div class="row">
      <div v-bind:class="col-sm-10">
        <hr>
        <hr>
        <hr>
        <hr>
        <h1>Heart Disease Dataset</h1>
        <!--
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Book</button>
        -->
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Index</th>
              <th scope="col">Age</th>
              <th scope="col">Sex</th>
              <th scope="col">Chest Pain Type</th>
              <th scope="col">Resting Blood Pressure</th>
              <th scope="col">Serum Cholestoral in mg/dl</th>
              <th scope="col">Fasting Blood Sugar > 120 mg/dl</th>
              <th scope="col">Resting Electrocardiographic Results</th>
              <th scope="col">Maximum Heart Rate Achieved</th>
              <th scope="col">Exercise Induced Angina</th>
              <th scope="col">Oldpeak</th>
              <th scope="col">The Slope of the Peak Exercise ST segment</th>
              <th scope="col">Number of Major Vessels (0-3) colored by Flourosopy</th>
              <th scope="col">Thalassemia</th>
              <th scope="col">Target:have disease</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data, index) in datasets" :key="index">
              <td>{{ index+1 }}</td>
              <td>{{ data.age }}</td>
              <td>{{ data.sex }}</td>
              <td>{{ data.chest }}</td>
              <td>{{ data.pressure }}</td>
              <td>{{ data.cholestoral }}</td>
              <td>{{ data.sugar }}</td>
              <td>{{ data.cardiographic }}</td>
              <td>{{ data.heart_rate }}</td>
              <td>{{ data.angina }}</td>
              <td>{{ data.oldpeak }}</td>
              <td>{{ data.slope }}</td>
              <td>{{ data.flourosopy }}</td>
              <td>{{ data.thal }}</td>
              <td>{{ data.target }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      datasets: [],
    };
  },
  methods: {
    getDatasets() {
      // const path = 'http://localhost:5000/datasets';
      const path = 'https://heart.unicornchatbot.com/datasets';
      axios.get(path)
        .then((res) => {
          this.datasets = res.data.datasets;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getDatasets();
  },
};
</script>


<style scoped>

.wrapper{
  background-color: #ffffff;
}

.container {
    /*width: 100%;
    height: 100%;*/
    padding-right: 15px;
    padding-left:  15px;
    margin-right: 10px;
    margin-left: 10px;
}
.table thead th {
    vertical-align: middle;
    border-bottom: 2px solid #dee2e6;
}
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

</style>
