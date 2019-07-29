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

The backend is a [Flask](https://palletsprojects.com/p/flask/) application run within [Docker](https://www.docker.com/).

To run locally, 

```bash
cd backend
docker-compose build
docker-compose up
```

Note that the `app` and `models` directories are mapped in as volumes. Thus, the app will reload when you edit application code. Also, you must have a model present in the `models` directory for the app to run.

### Frontend

The frontend is a [Vue.js](https://vuejs.org/) single page application.

To run locally,

```bash
cd frontend
yarn install
yarn serve
```


