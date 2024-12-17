SELECT 
    transaction_id,
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    DAY(transaction_date) AS day,
    QUARTER(transaction_date) AS quarter,
    WEEKDAY(transaction_date) AS weekday
FROM eT3Cash.Transactions;