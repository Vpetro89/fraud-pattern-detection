SELECT
    account_id,
    COUNT(*) AS transactions_last_hour
FROM transactions
WHERE transaction_time >= NOW() - INTERVAL '1 hour'
GROUP BY account_id
ORDER BY transactions_last_hour DESC;