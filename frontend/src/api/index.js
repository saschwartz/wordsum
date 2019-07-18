import axios from 'axios'

const apiClient = axios.create({
  baseURL: process.env.NODE_ENV === 'local' ? 'http://localhost:8000' : 'http://production.api.url.here', 
  timeout: 1000,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS'
  }
})

export { apiClient }
