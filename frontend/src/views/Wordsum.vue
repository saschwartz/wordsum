<template lang='pug'>
  div#wordsum
    div#instructions
      p Try make a word equation that sums up to the target word!
    div#input-container
      div#target-container
        div(v-if='target')
          p Try make:
            span#target &nbsp {{ target }}
        div(v-else)
          p You've completed all the target words! Try experimenting with other word equations.
      div#equation-container(:class='equationClass')
        input(v-model='wordInput', placeholder='e.g. king + woman - man', :class='equationClass')
        div(:class='equationClass')#equals &nbsp = {{ mostSimilar.length > 0 ? mostSimilar[0][0] : "??????" }}
      div(v-if='targetInInput')#error-text You can't put the target word in the equation!
    div#equations 
      h3 Your successful equations:
      transition-group(name='equations')
        p(v-for='e in equations', :key='e') {{ e }}

</template>

<script>
import { apiClient } from '@/api'

export default {
  name: 'wordsum',
  data () {
    return {
      mostSimilar: [],
      wordInput: '',
      target: 'queen',
      availableTargets: [
        'surgeon', 'pediatrician', 'dentist', 'ambulance', 'mother', 'father',
        'cardiologist', 'psychiatrist', 'dermatologist', 'neurologist'
      ],
      equationClass: 'pending',
      equations: []
    }
  },
  computed: {
    wordEquation: function () {
      let positive = []
      let negative = []
      let tokens = this.wordInput
        .replace(/[.,/#!$%^&*;:{}=_`~()]/g, '')
        .toLowerCase()
        .split(' ')
        .filter((x) => x.length > 0)
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
    },
    targetInInput: function () {
      return this.wordEquation.positive.includes(this.target) || this.wordEquation.negative.includes(this.target)
    }
  },
  methods: {
    shuffle (a) {
      // shuffle an array in place
      for (let i = a.length - 1; i > 0; i--) {
        let r = Math.floor(Math.random() * (i + 1))
        let tmp = a[i]
        a[i] = a[r]
        a[r] = tmp
      }
      return a
    },
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
      if (Array.from(this.mostSimilar, x => x[0].toLowerCase()).includes(this.target) && !this.targetInInput) {
        this.equationClass = 'success'
        setTimeout(() => {
          this.equations.push(this.wordInput + ' = ' + this.target)
          this.wordInput = ''
          this.target = this.availableTargets.pop()
        }, 1000)
      } else if (this.targetInInput) {
        this.equationClass = 'error'
      } else {
        this.equationClass = 'pending'
      }
    }
  },
  mounted () {
    this.shuffle(this.availableTargets)
  }
}
</script>

<style lang='scss'>
@import '~@/styles/fonts';
@import '~@/styles/layout';
@import '~@/styles/variables';

#wordsum {
  display: flex;
  flex-direction: column;

  input:focus {
    outline-width: 0;
  }

  #instructions {
    line-height: 1.2rem;
    font-size: 1.1rem;

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

  #input-container {
    #target-container {
      text-align: center;
      font-size: 1.3rem;
      #target {
        color: $theme-secondary-color;
        font-weight: bold;
      }
    }

    #equation-container {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;

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
        min-width: 150px;
      }
    }

    #error-text {
      padding-top: 5px;
      color: $theme-error-color;
      font-size: 1rem;
      text-align: center;
    }
  }

  #equations {
    margin-top: 30px;
    margin-bottom: 10px;
    h3 {
      margin-bottom: 10px;
    }
    p {
      color: $theme-success-color;
      font-weight: bold;
      font-size: 1.1rem;
      margin-bottom: 0;
    }

    .equations-item {
      display: inline-block;
      margin-right: 10px;
    }
    .equations-enter-active, .equations-leave-active {
      transition: all 1s;
    }
    .equations-enter, .equations-leave-to /* .list-leave-active below version 2.1.8 */ {
      opacity: 0;
      transform: translateY(30px);
    }
  }
}

</style>
