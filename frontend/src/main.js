import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

// devtools on if local
if (process.env.NODE_ENV === 'local') { Vue.config.devtools = true }

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
