# wordsum

## Overview

Web application for exploring the vector additive properties of word2vec

[Gensim](https://radimrehurek.com/gensim/index.html), a Python library used to do semantic analyis of text, is useed with Google's [News Vectors Dataset](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM) to provide the backend of this app. 

The frontend is build using [VueJS](https://vuejs.org/).

Users are given a target word that they must build using a word equation. For example:

```
king - man + woman = queen
```

This is possible because of the vector additive properties of word embeddings. Though there are a few caveats to describing word embeddings as living in a 'vector space', it is still a good descriptor.

## Developing Locally

### Backend

The backend is a [Flask](https://palletsprojects.com/p/flask/) application. You can run it with [Docker](https://hub.docker.com/) with:

```bash
cd backend
docker-compose up
```

Note that you must have a model present in the `models` directory for the app to run when using Docker. The Google Cloud SDK version will use a hosted version of the model, so you don't have to worry if running that way.

The model file itself that is running in production can be found [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)

### Frontend

The frontend is a [Vue.js](https://vuejs.org/) single page application.

To run locally,

```bash
cd frontend
yarn install
yarn serve
```


