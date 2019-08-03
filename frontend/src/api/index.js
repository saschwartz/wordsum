import axios from 'axios'

const apiClient = axios.create({
  baseURL: process.env.NODE_ENV === 'local' ? 'http://localhost:8082' : 'https://wordsum-api.sebschwartz.me',
  timeout: 1000,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS'
  }
})

export { apiClient }
