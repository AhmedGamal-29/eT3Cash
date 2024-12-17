SELECT 
    dt.date_key, 
    SUM(t.amount) AS total_amount
FROM 
    DimTime dt
LEFT JOIN 
    eT3Cash.Transactions t ON DATE(t.transaction_date) = dt.date_key
GROUP BY 
    dt.date_key
ORDER BY 
    dt.date_key DESC;
-- It gets all transactions done and amount in every day