<template lang='pug'>
  div#app
    div#main-content-container
      div#main-content-inner
        div#page-content
          h1 Wordsum
          div#nav-container
            hr
            div#nav-links
              div.nav-link
                router-link(to='/wordsum') Wordsum
              div.nav-link
                router-link(to='/about') About
            hr
          transition(name="fade" mode="out-in")
            router-view
        Footer
</template>

<script>
import Footer from './components/Footer'

export default {
  name: 'App',
  components: { Footer }
}
</script>

<style lang='scss'>
@import '~@/styles/fonts';
@import '~@/styles/layout';
@import '~@/styles/variables';

/* transition styling */
.fade-enter {
  opacity: 0;
}
.fade-enter-active {
  transition: opacity 0.2s ease;
} 
.fade-leave-active {
  transition: opacity 0.2s ease;
  opacity: 0;
}

#app {
  background: rgba($theme-secondary-color, 0.2);
}

#nav-container {
  margin-bottom: 30px;

  a {
    color: inherit;
    text-decoration: none;
  }

  #nav-links {
    display: flex;
    flex-wrap: wrap;
    .nav-link {
      margin-right: 25px;
    }
    .router-link-active {
      font-weight: bold;
      color: $theme-secondary-color;
    }
  }
}

// separate out page content
#main-content-container {
  margin: auto;
  max-width: 1100px;
  height: 100vh;

  #main-content-inner {
    overflow:auto;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    position: relative;
    background: rgba(255, 255, 255, 0.92);
    z-index: 10;
    height: 100%;

    #page-content {
      padding-left: 3rem;
      padding-right: 3rem;
      margin-top: 30px;
    }
  }
}

</style>
