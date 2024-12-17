<template>
  <div class="transfer-container">
    <div class="transfer-header">
      <h2>Transfer Funds</h2>
    </div>
    <form @submit.prevent="transfer" class="transfer-form">
      <div class="input-container">
        <input
          id="amount"
          v-model="amount"
          type="number"
          placeholder="Enter amount to transfer"
          min="1"
          step="0.01"
          required
          class="input-field"
        />
      </div>
      <div class="input-container">
        <input
          id="recipient"
          v-model="recipient"
          type="text"
          placeholder="Enter recipient's username"
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
      recipient: '',
      loading: false,
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    async transfer() {
      this.loading = true;
      this.successMessage = '';
      this.errorMessage = '';

      try {
        const token = localStorage.getItem('token');
        const response = await axios.post('http://127.0.0.1:8000/api/transfer/', {
          amount: this.amount,
          transaction_type:"transfer",
          recipient: {username: this.recipient},
        }, {
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        this.successMessage = `Successfully transferred $${this.amount} to ${this.recipient}.`;
        this.amount = ''; 
        this.recipient = ''; 
      } catch (error) {
        this.errorMessage = error.response?.data?.message || 'Transfer failed. Please try again.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.transfer-container {
  max-width: 500px;
  margin: 50px auto;
  padding: 30px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.transfer-header h2 {
  font-size: 2em;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
}

.transfer-form {
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
  .transfer-container {
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
