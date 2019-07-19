<template lang='pug'>
  div#wordsum
    p Input a word equation, for example "king + woman - man", to see the most similar words as calculated by word2vec.
    div#equation-container
      input(v-model='wordInput')
    div(v-if='mostSimilar.length > 0')#similar-results
      h4 Top Results
      div#result(v-for='word in mostSimilar')
        span#result-word {{ word[0] }}
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
      let tokens = this.wordInput.split(' ').filter((x) => x.length > 0)
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

<style lang='scss'>
@import '~@/styles/fonts';
@import '~@/styles/layout';
@import '~@/styles/variables';

#wordsum {
  width: 100%;

  input:focus {
    outline-width: 0;
  }

  #equation-container {
    width: 100%;

    input {
      padding: 20px;
      width: 100%;
      font-size: 1.75rem;
      height: 3.5rem;
      color: $theme-secondary-color;
      border: solid 2px $theme-secondary-color;
      border-radius: 10px;
      -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
      -moz-box-sizing: border-box;    /* Firefox, other Gecko */
      box-sizing: border-box;         /* Opera/IE 8+ */
    }
  }

  #similar-results {
    #result {
      #result-word {
        color: $theme-secondary-color;
        font-weight: bold;
      }
    }
  }
}

</style>
