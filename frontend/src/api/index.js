import { axios } from 'axios'

const apiClient = axios.create({
  baseUrl: process.env.NODE_ENV === 'local' ? 'http://localhost:8000' : 'http://production.api.url.here', 
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' }
})

export { apiClient }
