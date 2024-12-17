SELECT 
    COUNT(t.transaction_id) AS num_transactions,
    SUM(t.amount) AS total_amount
FROM 
    eT3Cash.Transactions t
WHERE 
    YEAR(t.transaction_date) = 2024 AND QUARTER(t.transaction_date) = 4;
-- Highest Quarter 