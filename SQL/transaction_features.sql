SELECT
    account_id,
    COUNT(*) AS transaction_count,
    AVG(amount) AS avg_transaction_amount,
    MAX(amount) AS max_transaction_amount,
    COUNT(DISTINCT ip_country) AS country_count,
    COUNT(DISTINCT device_id) AS device_count
FROM transactions
GROUP BY account_id;