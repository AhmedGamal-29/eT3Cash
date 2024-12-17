SELECT 
    c.customer_name, 
    COUNT(t.transaction_id) AS num_transactions
FROM 
    eT3Cash.Customer c
LEFT JOIN
	eT3Cash.Wallet w ON w.customer_id = c.customer_id
LEFT JOIN 
    eT3Cash.Transactions t ON c.customer_id = t.wallet_id
GROUP BY 
    c.customer_name
ORDER BY 
    num_transactions DESC
LIMIT 10;

-- It gets top 10 customers used the service
