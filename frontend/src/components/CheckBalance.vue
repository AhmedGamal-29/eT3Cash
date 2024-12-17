<template>
  <div class="balance-container">
    <div class="logo">
      <img src="@/assets/logo.png" alt="ET3 Logo" />
    </div>
    <div class="balance-header">
      <h2>Check Balance</h2>
    </div>
    <div class="balance-action">
      <button @click="checkBalance" class="check-balance-button" :disabled="loading">
        <span v-if="loading" class="loader"></span>
        <span v-else>Check Balance</span>
      </button>
    </div>
    <div v-if="balance !== null && !loading" class="balance-display">
      Your balance is: <strong>${{ balance }}</strong>
    </div>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      balance: null,
      loading: false,
      errorMessage: '',
    };
  },
  methods: {
    async checkBalance() {
      this.loading = true;
      this.errorMessage = '';

      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://127.0.0.1:8000/api/check-balance/', {
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        this.balance = response.data.balance;
      } catch (error) {
        this.errorMessage = error.response?.data?.message || 'Failed to check balance. Please try again.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.balance-container {
  max-width: 500px;
  margin: 50px auto;
  padding: 30px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.balance-header h2 {
  font-size: 2em;
  margin-bottom: 20px;
  color: #333;
}

.check-balance-button {
  background-color: #6200ee;
  color: white;
  padding: 14px 20px;
  font-size: 1em;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.check-balance-button:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.check-balance-button:hover:enabled {
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

.balance-display {
  margin-top: 20px;
  font-size: 1.5em;
  color: #333;
}

.error-message {
  color: #dc3545;
  font-weight: bold;
  margin-top: 20px;
}

@media (max-width: 480px) {
  .balance-container {
    padding: 20px;
  }

  .check-balance-button {
    padding: 12px 15px;
    font-size: 0.9em;
  }

  .balance-display {
    font-size: 1.2em;
  }
}
</style>
