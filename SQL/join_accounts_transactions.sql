SELECT
    t.transaction_id,
    t.account_id,
    a.home_country,
    a.industry,
    t.amount,
    t.transaction_time,
    t.is_fraud_txn
FROM transactions t
INNER JOIN accounts a
    ON t.account_id = a.account_id;