<template lang='pug'>
  div {{ mostSimilar }}
</template>

<script>
import { apiClient } from '@/api'

export default {
  name: 'wordsum',
  data () {
    return {
      mostSimilar: []
    }
  },
  methods: {
    getMostSimilar ({ positive, negative, count }) {
      apiClient.post('/most_similar', { positive, negative, count })
        .then((response) => {
          this.mostSimilar = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  mounted () {
    this.getMostSimilar({ positive: ['king', 'woman'], negative: ['man'], count: 5 })
  }
}
</script>
