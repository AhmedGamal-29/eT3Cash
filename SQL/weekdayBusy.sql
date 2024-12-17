SELECT 
    dt.weekday, 
    COUNT(t.transaction_id) AS num_transactions
FROM 
    DimTime dt
LEFT JOIN 
    eT3Cash.Transactions t ON DATE(t.transaction_date) = dt.date_key
GROUP BY 
    dt.weekday
ORDER BY 
    num_transactions DESC;