<template>
  <div class="login-container">
    <div class="logo">
      <img src="@/assets/logo.png" alt="ET3 Logo" />
    </div>
    <h2 class="login-header">Login</h2>
    <form @submit.prevent="handleLogin" class="login-form">
      <div class="input-container">
        <input
          v-model="username"
          type="text"
          id="username"
          required
          class="input-field"
          placeholder="Username"
        />
      </div>
      <div class="input-container">
        <input
          v-model="password"
          type="password"
          id="password"
          required
          class="input-field"
          placeholder="Password"
        />
      </div>
      <button type="submit" class="submit-button">Login</button>
    </form>
    <router-link to="/register" class="btn btn-link">Register Here</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          username: this.username,
          password: this.password,
        });

        const token = response.data.token;
        localStorage.setItem('token', token); 

        // Redirect user to dashboard or home after login
        if (response.status === 200) {
          console.log('Login successful', response.data);
          this.$router.push('/dashboard');
        }
      } catch (error) {
        console.error('Login failed', error.response);
        alert('Login failed. Please check your username and password.');
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 30px; 
  background-color: #fff; 
  border-radius: 12px; 
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
  text-align: center; 
}

.logo img {
  max-width: 150px;
  margin-bottom: 20px;
}

.login-header {
  font-size: 2em; /* Larger font size for header */
  margin-bottom: 20px;
  color: #333; /* Dark text color */
}

.login-form {
  display: flex;
  flex-direction: column; /* Column layout for inputs */
  gap: 15px; /* Space between inputs */
}

.input-container {
  position: relative; /* For label positioning */
}

.input-label {
  position: absolute;
  top: -12px;
  left: 20px;
  background-color: #fff;
  padding: 0 5px;
  color: #6200ee; /* Blue label color */
  font-size: 0.9em; /* Smaller font for label */
}

.input-field {
  width: 100%;
  padding: 14px;
  border: 2px solid #ddd; /* Light border */
  border-radius: 10px; /* Rounded corners */
  outline: none; /* Remove default outline */
  font-size: 1em; /* Default font size */
  transition: border-color 0.3s; /* Smooth transition */
}

.input-field:focus {
  border-color: #6200ee; /* Change border color on focus */
}

.submit-button {
  background-color: #007bff; /* Bootstrap primary color */
  color: white;
  padding: 14px;
  font-size: 1em;
  border: none; 
  border-radius: 10px; 
  cursor: pointer; 
  transition: background-color 0.3s, transform 0.2s;
}

.submit-button:hover {
  background-color: #0056b3; 
  transform: translateY(-2px); 
}

.btn-link {
  margin-top: 10px; 
  color: #007bff; 
  text-decoration: none; 
}

.btn-link:hover {
  text-decoration: underline; 
}

@media (max-width: 480px) {
  .login-container {
    padding: 20px; /* Less padding on smaller screens */
  }
  .input-field {
    padding: 12px; /* Adjust padding */
  }
  .submit-button {
    font-size: 0.9em; /* Slightly smaller font size */
    padding: 12px; /* Adjust padding */
  }
}
</style>
