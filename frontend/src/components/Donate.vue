<template>
  <div class="donate-container container">
    <div class="logo">
      <img src="@/assets/logo.png" alt="ET3 Logo" />
    </div>
    <div class="donate-header header">
      <h2>Donate</h2>
    </div>
    <form @submit.prevent="donate" class="donate-form form">
      <div class="input-container">
        <input
          id="amount"
          v-model="amount"
          type="number"
          placeholder="Enter donation amount"
          required
          class="input-field"
        />
      </div>
      <button type="submit" class="submit-button" :disabled="loading">
        <span v-if="loading" class="loader"></span>
        <span v-else>Submit Donation</span>
      </button>
      <div v-if="message" class="success-message">{{ message }}</div>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import '@/assets/styles/shared.css'; // Import the shared styles

export default {
  data() {
    return {
      amount: 0,
      message: '',
      errorMessage: '',
      loading: false,
    };
  },
  methods: {
    async donate() {
      this.loading = true;
      this.message = '';
      this.errorMessage = '';

      try {
        const token = localStorage.getItem('token');
        const response = await axios.post('http://127.0.0.1:8000/api/donate/', {
          amount: this.amount,
          transaction_type: "donation"
        }, {
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        this.message = `Successfully donated $${this.amount}. Thank you!`;
        this.amount = 0; // Reset amount
      } catch (error) {
        this.errorMessage = error.response?.data?.message || 'Donation failed. Please try again.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>