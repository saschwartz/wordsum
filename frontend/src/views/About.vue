<template lang='pug'>
  div
    h2 Word2Vec Models
    p
    | The back end of this application exposes an API to a 
    a(href='https://en.wikipedia.org/wiki/Word2vec', target='_blank') word2vec
    |  model. These models work by turning words in a corpus into high dimensional vectors. The models thus live in a vector space. See the original paper here: 
    a(href='https://arxiv.org/abs/1301.3781', target='_blank') Efficient Estimation of Word Representations in Vector Space
    | . Word2Vec models can use either of two structures. Either they predict a word given the words around it, known as a 'continuous bag of words' method, or they use a word to predict its context, known as a 'skip-gram' method.
    p
    | Because the model lives in a vector space, vector operations can essentially be performed on words using this model. Very interestingly, performing such operations may even have semantic meaning in a linguistic sense. This is what this particular application explores, by allowing users to add up 'word equations'. This addition happens in a vector space, and the nearest word is then found using the 
    a(href='https://pypi.org/project/gensim/') gensim
    |  library. Read more on the topic here: 
    a(href='https://www.aclweb.org/anthology/N13-1090') Linguistic Regularities in Continuous Space Word Representations
    | .

    h2 Author and Code
    p
    | This application was authored by 
    a(href='https://sebschwartz.me', target='_blank') Sebastian Schwartz
    | . 
    p
    | The source lives 
    a(href='https://github.com/saschwartz/wordsum', target='_blank') here
    | .
  
</template>

<script>

export default {
  name: 'about'
}
</script>
