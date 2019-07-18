<template lang='pug'>
  div
    p Input a word equation, for example "king + woman - man", to see the most similar words as calculated by word2vec.
    input(v-model='wordInput')
    ul
      li(v-for='word in mostSimilar') {{ word[0] }} (score:  {{ parseFloat(word[1]).toFixed(3) }} )
</template>

<script>
import { apiClient } from '@/api'

export default {
  name: 'wordsum',
  data () {
    return {
      mostSimilar: [],
      wordInput: ''
    }
  },
  computed: {
    wordEquation: function () {
      let positive = []
      let negative = []
      let tokens = this.wordInput.split(' ')
      let add = true
      let subtract = false
      for (let i = 0; i < tokens.length; i++) {
        if (tokens[i] === '+') {
          add = true
          subtract = false
        } else if (tokens[i] === '-') {
          add = false
          subtract = true
        } else if (add) {
          positive.push(tokens[i])
        } else if (subtract) {
          negative.push(tokens[i])
        }
      }
      console.log(tokens)
      console.log({ positive, negative })
      return { positive, negative }
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
  watch: {
    wordEquation () {
      this.getMostSimilar({ positive: this.wordEquation.positive, negative: this.wordEquation.negative, count: 5 })
    }
  }
}
</script>
