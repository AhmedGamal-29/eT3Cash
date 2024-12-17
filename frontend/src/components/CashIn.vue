<template>
  <div class="cashin-container">
    <div class="logo">
      <img src="@/assets/logo.png" alt="ET3 Logo" />
    </div>
    <div class="cashin-header">
      <h2>Cash In</h2>
    </div>
    <form @submit.prevent="cashIn" class="cashin-form">
      <div class="input-container">
        <input 
          v-model="amount" 
          type="number" 
          id="amount"
          placeholder="Enter the amount"
          min="1"
          step="1"
          required 
          class="input-field"
        />
      </div>
      <button type="submit" class="submit-button" :disabled="loading">
        <span v-if="loading" class="loader"></span>
        <span v-else>Submit</span>
      </button>
      <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      amount: '',
      loading: false,
      successMessage: '',
      errorMessage: ''
    };
  },
  methods: {
    async cashIn() {
      this.loading = true;
      this.successMessage = '';
      this.errorMessage = '';
      try {
        const token = localStorage.getItem('token');
        const response = await axios.post('http://127.0.0.1:8000/api/cash-in/', {
          amount: this.amount,transaction_type:"cash_in"
        }, {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        this.successMessage = 'Cash In successful!';
        this.amount = ''; 
      } catch (error) {
        this.errorMessage = error.response?.data?.message || 'Transaction failed. Please try again.';
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.cashin-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 30px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.cashin-header h2 {
  font-size: 2em;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
}

.cashin-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-container {
  position: relative;
}

.input-label {
  position: absolute;
  top: -12px;
  left: 20px;
  background-color: #fff;
  padding: 0 5px;
  color: #6200ee;
  font-size: 0.9em;
}

.input-field {
  width: 100%;
  padding: 14px;
  border: 2px solid #ddd;
  border-radius: 10px;
  outline: none;
  font-size: 1em;
  transition: border-color 0.3s;
}

.input-field:focus {
  border-color: #6200ee;
}

.submit-button {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #6200ee;
  color: white;
  padding: 14px;
  font-size: 1em;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.submit-button:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.submit-button:hover:enabled {
  background-color: #5300d1;
  transform: translateY(-2px);
}

.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #fff;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.success-message {
  text-align: center;
  color: #28a745;
  font-weight: bold;
}

.error-message {
  text-align: center;
  color: #dc3545;
  font-weight: bold;
}

@media (max-width: 480px) {
  .cashin-container {
    padding: 20px;
  }
  .input-field {
    padding: 12px;
  }
  .submit-button {
    font-size: 0.9em;
    padding: 12px;
  }
}
</style>
