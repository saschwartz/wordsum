import Vue from 'vue'
import Router from 'vue-router'
import Wordsum from './views/Wordsum.vue'
import About from './views/About.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/wordsum',
      name: 'wordsum',
      component: Wordsum
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '*',
      name: 'all',
      component: Wordsum
    }
  ]
})
