<template>
  <div class="invest-container container">
    <div class="logo">
      <img src="@/assets/logo.png" alt="ET3 Logo" />
    </div>
    <div class="invest-header header">
      <h2>Invest Funds</h2>
    </div>
    <form @submit.prevent="invest" class="invest-form form">
      <div class="input-container">
        <input
          id="amount"
          v-model="amount"
          type="number"
          placeholder="Enter amount to invest"
          required
          class="input-field"
        />
      </div>
      <div class="input-container">
        <select v-model="selectedSymbol" required class="input-field">
          <option disabled value="">Select a stock to invest in</option>
          <option v-for="(stock, symbol) in marketData" :key="symbol" :value="symbol">
            {{ symbol }} - {{ stock.name }} (${{ stock.price }})
          </option>
        </select>
      </div>
      <button type="submit" class="submit-button" :disabled="loading">
        <span v-if="loading" class="loader"></span>
        <span v-else>Submit Investment</span>
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
      selectedSymbol: '',
      marketData: {}, // This will hold the stock data
      message: '',
      errorMessage: '',
      loading: false,
    };
  },
  async mounted() {
    await this.fetchMarketData(); // Fetch market data on component mount
  },
  methods: {
    async fetchMarketData() {
  try {
    const token = localStorage.getItem('token'); // Retrieve token from localStorage
    const response = await axios.get('http://127.0.0.1:8000/api/market-data/', {
      headers: {
        'Authorization': `Token ${token}`,
      },
    });
    this.marketData = response.data;
  } catch (error) {
    console.error('Failed to fetch market data:', error);
    this.errorMessage = 'Could not load market data. Please try again later.';
  }
},
    async invest() {
      this.loading = true;
      this.message = '';
      this.errorMessage = '';

      try {
        const token = localStorage.getItem('token');
        const response = await axios.post('http://127.0.0.1:8000/api/invest/', {
          amount: this.amount,
          transaction_type: "investment",
          symbol: this.selectedSymbol, // Include selected stock symbol in the request
        }, {
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        this.message = `Successfully invested $${this.amount} in ${this.selectedSymbol}. Thank you for your investment!`;
        this.amount = 0; // Reset amount
        this.selectedSymbol = ''; // Reset selected stock
      } catch (error) {
        this.errorMessage = error.response?.data?.message || 'Investment failed. Please try again.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>