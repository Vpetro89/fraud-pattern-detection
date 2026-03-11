WITH features AS (
    SELECT
        account_id,
        COUNT(*) AS transaction_count,
        AVG(amount) AS avg_amount,
        MAX(amount) AS max_amount,
        COUNT(DISTINCT ip_country) AS country_count
    FROM transactions
    GROUP BY account_id
)

SELECT *
FROM features
WHERE transaction_count > 25
   OR max_amount > 1500
   OR country_count > 2
ORDER BY transaction_count DESC;