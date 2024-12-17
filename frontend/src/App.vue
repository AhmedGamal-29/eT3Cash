<template>
  <div id="app">
    <header class="header">
      <img src="@/assets/logo.png" alt="ET3 Logo" class="logo" />
    </header>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}

.header {
  background: #007bff;
  padding: 10px;
}

.logo {
  height: 50px;
}
</style>
