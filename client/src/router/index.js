import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Home from '@/components/Home';
import Planet from '@/components/Planet';
import Stats from '@/components/Stats';
import Predict from '@/components/Predict';
import Test from '@/components/Test';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/stats',
      name: 'Stats',
      component: Stats,
    },
    {
      path: '/planet',
      name: 'Planet',
      component: Planet,
    },
    {
      path: '/predict',
      name: 'Predict',
      component: Predict,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
  ],
});
