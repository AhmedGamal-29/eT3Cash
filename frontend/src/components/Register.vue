<template>
  <div class="register-container">
    <div class="logo">
      <img src="@/assets/logo.png" alt="ET3 Logo" />
    </div>
    <h2 class="register-header">Register</h2>
    <form @submit.prevent="handleRegister" class="register-form">
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
          v-model="email"
          type="email"
          id="email"
          required
          class="input-field"
          placeholder="Email Address"
        />
      </div>
      <div class="input-container">
        <input
          v-model="phone"
          type="tel"
          id="phone"
          required
          class="input-field"
          placeholder="Phone Number"
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
      <button type="submit" class="submit-button">Register</button>
    </form>
    <router-link to="/" class="btn btn-link">Already have an account? Login Here</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Register',
  data() {
    return {
      username: '',
      email: '',
      phone: '',
      password: ''
    };
  },
  methods: {
    async handleRegister() {
      try {
        
        const response = await axios.post('http://127.0.0.1:8000/api/register/', {
          username: this.username,
          email: this.email,
          phone: this.phone,
          password: this.password,
        });

        
        if (response.status === 201) {
          console.log('Registration successful', response.data);
          alert('Registration successful! Please login.');
          
          this.$router.push('/login');
        }
      } catch (error) {
        // Enhanced error handling
        if (error.response) {
          console.error('Registration failed', error.response.data);
          alert(`Registration failed: ${error.response.data.detail || error.response.data}`);
        } else if (error.request) {
          console.error('No response received', error.request);
          alert('No response from the server. Please try again later.');
        } else {
          console.error('Error', error.message);
          alert(`An error occurred: ${error.message}`);
        }
      }
    }
  }
};
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 50px auto; /* Center vertically */
  padding: 30px; /* More padding for better spacing */
  background-color: #fff; /* White background */
  border-radius: 12px; /* Rounded corners */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  text-align: center; /* Center text */
}

.logo img {
  max-width: 150px;
  margin-bottom: 20px;
}

.register-header {
  font-size: 2em; /* Larger font size for header */
  margin-bottom: 20px;
  color: #333; /* Dark text color */
}

.register-form {
  display: flex;
  flex-direction: column; 
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
  border: none; /* No border */
  border-radius: 10px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  transition: background-color 0.3s, transform 0.2s; /* Smooth transition */
}

.submit-button:hover {
  background-color: #0056b3; /* Darker blue on hover */
  transform: translateY(-2px); /* Slight upward movement */
}

.btn-link {
  margin-top: 10px; /* Space above the link */
  color: #007bff; /* Bootstrap link color */
  text-decoration: none; /* No underline */
}

.btn-link:hover {
  text-decoration: underline; /* Underline on hover */
}

@media (max-width: 480px) {
  .register-container {
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
