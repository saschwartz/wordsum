<template lang='pug'>
  div#footer
    div#inner-footer
      div#copyright © {{ new Date().getFullYear() }} Sebastian Schwartz
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style lang='scss'>
@import '~@/styles/fonts';
@import '~@/styles/layout';
@import '~@/styles/variables';

#footer {
  width: 100%;
  margin-top: 2rem;
  background-color: $theme-primary-color;
  text-align: center;
  vertical-align: middle;
  color: #fff;
  display: flex;
  flex-direction: column;
  padding: 0.75rem 0;

  #inner-footer {
    margin: 0 3rem;
  }
}

</style>
