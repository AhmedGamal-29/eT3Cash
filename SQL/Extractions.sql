SELECT customer_id, username, customer_name, email, phone_number, created_at
FROM eT3Cash.Customer;

SELECT wallet_id, customer_id, balance, created_at
FROM eT3Cash.Wallet;

SELECT transaction_id, wallet_id, transaction_date, amount
FROM eT3Cash.Transactions;

