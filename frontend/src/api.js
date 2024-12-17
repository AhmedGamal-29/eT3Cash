/*
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',  // Django backend URL
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,  // This enables sending cookies with requests (for authentication)
});

// Intercept requests to include authorization token if it exists
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers['Authorization'] = `Token ${token}`;
  }
  return config;
});

export default apiClient;
*/