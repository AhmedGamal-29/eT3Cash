import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import Dashboard from '@/components/Dashboard.vue';
import CashIn from '@/components/CashIn.vue';
import CheckBalance from './components/CheckBalance.vue';
import CashOut from '@/components/CashOut.vue'; 
import Transfer from '@/components/Transfer.vue'; 
import Donate from '@/components/Donate.vue'; 
import Invest from '@/components/Invest.vue'; 
import Transactions from '@/components/Transactions.vue'; 

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/cash-in', name: 'CashIn', component: CashIn },
  { path: '/cash-out', name: 'CashOut', component: CashOut },
  { path: '/transfer', name: 'Transfer', component: Transfer }, 
  { path: '/donate', name: 'Donate', component: Donate },
  { path: '/invest', name: 'Invest', component: Invest }, 
  { path: '/transactions', name: 'Transactions', component: Transactions }, 
  { path: '/check-balance', name: 'CheckBalance', component: CheckBalance }, 

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
