CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_open_date DATE,
    home_country VARCHAR(10),
    customer_age INT,
    income_band INT,
    industry VARCHAR(50),
    is_fraud_account INT
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_time TIMESTAMP,
    amount NUMERIC(12,2),
    merchant_category VARCHAR(50),
    ip_country VARCHAR(10),
    device_id VARCHAR(50),
    channel VARCHAR(20),
    is_fraud_txn INT
);