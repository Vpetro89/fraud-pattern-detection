CREATE TABLE account_features AS
SELECT
    t.account_id,
    COUNT(*) AS txn_count,
    AVG(t.amount) AS avg_amount,
    MAX(t.amount) AS max_amount,
    COUNT(DISTINCT t.ip_country) AS country_count,
    COUNT(DISTINCT t.device_id) AS device_count,
    SUM(CASE WHEN t.is_fraud_txn = 1 THEN 1 ELSE 0 END) AS fraud_txn_count
FROM transactions t
GROUP BY t.account_id;