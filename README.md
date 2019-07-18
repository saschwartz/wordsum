# wordsum

## Overview

Web application for exploring the vector additive properties of word2vec

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


