import axios from 'axios'

const apiClient = axios.create({
  baseURL: process.env.NODE_ENV === 'local' ? 'http://localhost:8082' : 'https://personal-site-236718.appspot.com',
  timeout: 1000,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS'
  }
})

export { apiClient }
