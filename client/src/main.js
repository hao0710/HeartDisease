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
import SampleChartjs from './components/utilComponents/SampleChartjs.vue';
import SampleVueChartjs from './components/utilComponents/SampleVueChartjs.vue';
import SampleVueScatter from './components/utilComponents/SampleVueScatter.vue';
import BloodPressureVueScatter from './components/utilComponents/BloodPressureVueScatter.vue';
import CholestoralVueScatter from './components/utilComponents/CholestoralVueScatter.vue';
import HeartRateVueScatter from './components/utilComponents/HeartRateVueScatter.vue';
import OldpeakVueScatter from './components/utilComponents/OldpeakVueScatter.vue';
import ChestPainVueBar from './components/utilComponents/ChestPainVueBar.vue';
import FastBloodSugarVueBar from './components/utilComponents/FastBloodSugarVueBar.vue';
import CardiographicVueBar from './components/utilComponents/CardiographicVueBar.vue';
import AnginaVueBar from './components/utilComponents/AnginaVueBar.vue';
import SlopeVueBar from './components/utilComponents/SlopeVueBar.vue';
import FlourosopyPainVueBar from './components/utilComponents/FlourosopyPainVueBar.vue';
import SexVuePie from './components/utilComponents/SexVuePie.vue';
import ThalVuePie from './components/utilComponents/ThalVuePie.vue';
import Requestdata from './components/utilComponents/Requestdata.vue';
import Carousel from './components/Carousel.vue';
import VueCharts from 'vue-chartjs';
import planetChartData from './chart-data.js';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(VueCharts);

// register global components here
Vue.component('planetChartData', planetChartData);
Vue.component('SampleChart', SampleChart);
Vue.component('SampleChart1', SampleChart1);
Vue.component('Naviibar', Naviibar);
Vue.component('Carousel', Carousel);
Vue.component('Card', Card);
Vue.component('SampleChartjs', SampleChartjs);
Vue.component('SampleVueChartjs', SampleVueChartjs);
Vue.component('Requestdata', Requestdata);
Vue.component('SampleVueScatter', SampleVueScatter);
Vue.component('BloodPressureVueScatter', BloodPressureVueScatter);
Vue.component('CholestoralVueScatter', CholestoralVueScatter);
Vue.component('HeartRateVueScatter', HeartRateVueScatter);
Vue.component('OldpeakVueScatter', OldpeakVueScatter);
Vue.component('ChestPainVueBar', ChestPainVueBar);
Vue.component('FastBloodSugarVueBar', FastBloodSugarVueBar);
Vue.component('CardiographicVueBar', CardiographicVueBar);
Vue.component('AnginaVueBar', AnginaVueBar);
Vue.component('SlopeVueBar', SlopeVueBar);
Vue.component('FlourosopyPainVueBar', FlourosopyPainVueBar);
Vue.component('SexVuePie', SexVuePie);
Vue.component('ThalVuePie', ThalVuePie);






/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
