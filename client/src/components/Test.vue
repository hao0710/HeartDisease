<template>
    
  <div>
    <hr>
    <hr>
    <b-jumbotron header="Heart Disease Analysis" lead="Predict heart disease using machine learning"></b-jumbotron>
    <p>{{ data }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      data: [],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/datasets/blood';
      axios.get(path)
        .then((res) => {
          this.data = res.data.datasets;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>
</style>