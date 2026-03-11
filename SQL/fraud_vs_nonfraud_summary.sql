SELECT
    is_fraud_txn,
    COUNT(*) AS transaction_count,
    AVG(amount) AS avg_amount,
    MAX(amount) AS max_amount
FROM transactions
GROUP BY is_fraud_txn;