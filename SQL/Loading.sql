INSERT INTO DimCustomer (customer_id, username, customer_name, email, phone_number, created_at)
SELECT customer_id, username, customer_name, email, phone_number, created_at
FROM eT3Cash.Customer;


INSERT INTO data_warehouse.DimWallet (wallet_id, customer_id, balance, created_at)
SELECT wallet_id, customer_id, balance, created_at
FROM eT3Cash.Wallet;


INSERT INTO DimTime (date_key, year, month, day, quarter, weekday)
SELECT DISTINCT
    DATE(transaction_date) AS date_key,  -- Extracting only the date part
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    DAY(transaction_date) AS day,
    QUARTER(transaction_date) AS quarter,
    WEEKDAY(transaction_date) AS weekday
FROM eT3Cash.Transactions;
