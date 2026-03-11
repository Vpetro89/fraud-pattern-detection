SELECT account_id,
       account_open_date,
       home_country,
       customer_age,
       income_band,
       industry,
       is_fraud_account
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY account_id
               ORDER BY account_open_date DESC
           ) AS rn
    FROM accounts
) t
WHERE rn = 1;