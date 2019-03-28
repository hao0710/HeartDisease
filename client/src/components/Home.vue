<template>
  <div>
    <Naviibar></Naviibar>
    <Navbar></Navbar>
    <SampleChart></SampleChart>
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
a {
  color: #42b983;
}
</style>
