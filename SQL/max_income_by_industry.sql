SELECT
    industry,
    MAX(income_band) AS max_income
FROM accounts
GROUP BY industry
ORDER BY max_income DESC;