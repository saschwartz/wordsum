<template lang='pug'>
  div#wordsum
    div#instructions
      p Try make a word equation that sums up to the target word!
      p For example: 
        span#example-equation &nbsp king + woman - man = queen
    div#equation-container(:class='equationClass')
      input(v-model='wordInput', placeholder='e.g. king + woman - man', :class='equationClass')
      div(:class='equationClass')#equals &nbsp = {{ target }}
    div(v-if='mostSimilar.length > 0')#similar-results
      span Top Result: &nbsp
      span#result-word(v-for='(word, idx) in mostSimilar') {{ word[0] }}
        span(v-if='idx < mostSimilar.length - 1') ,&nbsp &nbsp
</template>

<script>
import { apiClient } from '@/api'
import styles from '@/styles/variables.scss'

export default {
  name: 'wordsum',
  data () {
    return {
      mostSimilar: [],
      wordInput: '',
      target: 'queen',
      availableTargets: ['surgeon', 'paediatrician', 'dentist', 'ambulance', 'mother', 'father'],
      equationClass: 'pending'
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
      this.getMostSimilar({ positive: this.wordEquation.positive, negative: this.wordEquation.negative, count: 1 })
    },
    mostSimilar () {
      let targetInInput = this.wordEquation.positive.includes(this.target) || this.wordEquation.negative.includes(this.target)
      if (Array.from(this.mostSimilar, x => x[0].toLowerCase()).includes(this.target) && !targetInInput) {
        this.equationClass = 'success'
      } else if (targetInInput) {
        this.equationClass = 'error'
      } else {
        this.equationClass = 'pending'
      }
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

  #instructions {
    line-height: 1.2rem;
    font-size: 1.2rem;
    #example-equation {
      color: $theme-secondary-color;
      font-weight: bold;
    }
  }

  .success {
    color: $theme-success-color;
  }
  .pending {
    color: $theme-secondary-color;
  }
  .error {
    color: $theme-error-color;
  }

  #equation-container {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    margin-top: 3rem;
    margin-bottom: 3rem;

    input {
      padding: 20px;
      max-width: 500px;
      flex: 1;
      height: 3.5rem;
      font-size: 1.3rem;
      border: solid 2px;
      border-radius: 10px;
      -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
      -moz-box-sizing: border-box;    /* Firefox, other Gecko */
      box-sizing: border-box;         /* Opera/IE 8+ */
    }

    #equals {
      font-size: 1.3rem;
      font-weight: bold;
    }
  }

  #similar-results {
    font-size: 1.2rem;
    margin-top: 30px;
    #result-word {
      color: $theme-secondary-color;
      font-weight: bold;
    }
  }
}

</style>
