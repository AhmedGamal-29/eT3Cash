<template>
  <div class="dashboard-container">
    <h1>Welcome to Et3 Cash </h1>
    <div class="sections">
      <div class="section">
        <router-link to="/cash-in" class="btn">Cash In</router-link>
        <router-link to="/cash-out" class="btn">Cash Out</router-link>
        <router-link to="/transfer" class="btn">Transfer</router-link>
      </div>
      <div class="section">
        <router-link to="/donate" class="btn">Donate</router-link>
        <router-link to="/invest" class="btn">Invest</router-link>
        <router-link to="/" class="btn">Logout</router-link>
      </div>
      <div class="section">
        <router-link to="/check-balance" class="btn">Check Balance</router-link>
        <router-link to="/transactions" class="btn">Transaction History</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard'
};
</script>

<style scoped>
.dashboard-container {
  text-align: center;
  padding: 20px;
}

.sections {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.section {
  background-color: #f8f9fa;
  border-radius: 10px;
  padding: 20px; 
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
  width: 250px; 
}

.section h2 {
  margin-bottom: 15px; 
}

.btn {
  display: block;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  margin-bottom: 10px;
  transition: background-color 0.3s; 
}

.btn:hover {
  background-color: #0056b3;
}
</style>
