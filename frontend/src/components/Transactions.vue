<template>
    <div class="transactions-container">
      <h2>Transaction History</h2>
      
      <div v-if="loading" class="loading">
        Loading transactions...
      </div>
      
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
  
      <table v-if="transactions.length && !loading && !errorMessage" class="transactions-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Type</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transaction in transactions" :key="transaction.id">
            <td>{{ formatDate(transaction.date) }}</td>
            <td>{{ transaction.transaction_type }}</td>
            <td>{{ formatCurrency(transaction.amount) }}</td>
            
          </tr>
        </tbody>
      </table>
      
      <div v-if="!transactions.length && !loading && !errorMessage" class="no-transactions">
        No transactions available.
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        transactions: [],
        loading: true,
        errorMessage: ''
      };
    },
    methods: {
      async fetchTransactions() {
        this.loading = true;
        this.errorMessage = '';
  
        try {
          const token = localStorage.getItem('token');
          const response = await axios.get('http://127.0.0.1:8000/api/transactions/', {
            headers: {
              'Authorization': `Token ${token}`
            }
          });
          this.transactions = response.data;
        } catch (error) {
          this.errorMessage = error.response?.data?.message || 'Failed to load transactions. Please try again later.';
        } finally {
          this.loading = false;
        }
      },
      formatDate(dateString) {
        const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
        return new Date(dateString).toLocaleDateString(undefined, options);
      },
      formatCurrency(amount) {
        return `$${parseFloat(amount).toFixed(2)}`;
      }
    },
    mounted() {
      this.fetchTransactions();
    }
  };
  </script>
  
  <style scoped>
  .transactions-container {
    max-width: 800px;
    margin: 50px auto;
    padding: 30px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  h2 {
    font-size: 2em;
    margin-bottom: 20px;
    color: #333;
  }
  
  .loading {
    font-size: 1.2em;
    color: #666;
  }
  
  .error-message {
    color: #dc3545;
    font-weight: bold;
    margin: 20px 0;
  }
  
  .transactions-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .transactions-table th,
  .transactions-table td {
    padding: 12px;
    border-bottom: 1px solid #ddd;
  }
  
  .transactions-table th {
    background-color: #6200ee;
    color: white;
    text-align: left;
  }
  
  .transactions-table tr:hover {
    background-color: #f1f1f1;
  }
  
  .no-transactions {
    font-size: 1.2em;
    color: #999;
    margin-top: 20px;
  }
  
  @media (max-width: 480px) {
    .transactions-container {
      padding: 20px;
    }
  
    .transactions-table th,
    .transactions-table td {
      padding: 10px;
      font-size: 0.9em;
    }
  }
  </style>
  