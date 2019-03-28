// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vue from 'vue';
import App from './App';
import router from './router';
import Navbar from './components/utilComponents/Navbar.vue';
import SampleChart from './components/utilComponents/SampleChart.vue';
import Naviibar from './components/Naviibar.vue';
import Carousel from './components/Carousel.vue';
import VueCharts from 'vue-chartjs';
import planetChartData from './chart-data.js';

Vue.config.productionTip = false;

Vue.use(BootstrapVue)

// register global components here
Vue.component('planetChartData', planetChartData);
Vue.component('Navbar', Navbar);
Vue.component('SampleChart', SampleChart);
Vue.component('Naviibar', Naviibar);
Vue.component('Carousel', Carousel);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
