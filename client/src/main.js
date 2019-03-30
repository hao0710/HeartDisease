// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vue from 'vue';
import App from './App';
import router from './router';
import Naviibar from './components/utilComponents/Naviibar.vue';
import Card from './components/utilComponents/Card.vue';
import SampleChart from './components/utilComponents/SampleChart.vue';
import SampleChart1 from './components/utilComponents/SampleChart1.vue';
import Carousel from './components/Carousel.vue';
import VueCharts from 'vue-chartjs';
import planetChartData from './chart-data.js';

Vue.config.productionTip = false;

Vue.use(BootstrapVue)

// register global components here
Vue.component('planetChartData', planetChartData);
Vue.component('SampleChart', SampleChart);
Vue.component('SampleChart1', SampleChart1);
Vue.component('Naviibar', Naviibar);
Vue.component('Carousel', Carousel);
Vue.component('Card', Card);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
