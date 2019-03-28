<template>
  <div>
    <ul>
      <li v-for="item in items" v-bind:key="item.name">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Navbar',
  data() {
    return {
      msg: 'I am the nav component',
      items: [
        { name: 'Nav1' },
        { name: 'Nav2' },
        { name: 'Nav3' },
        { name: 'Nav4' },
        { name: 'Nav5' },
        { name: 'Nav6' },
      ],
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
