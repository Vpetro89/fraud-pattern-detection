Fraud Pattern Detection Pipeline

Description
This project analyzes transaction behavior to identify accounts that show patterns consistent with fraud. Transaction features are engineered from raw data, then used to train a Random Forest classifier that scores each account for fraud risk.

Stack
Python
scikit-learn
pandas
matplotlib
Power BI

Pipeline
Transaction data is transformed into behavioral features.
Features are loaded into Python for model training.
A Random Forest model is trained to classify fraudulent vs normal accounts.
Class imbalance is handled using balanced class weights.
Model results are evaluated using classification metrics and a confusion matrix.
Fraud probabilities are generated and exported for analysis.

Model Features
total_transactions
total_spend
avg_transaction_amount
location_mismatch_count
distinct_devices

Outputs
fraud_predictions.csv with fraud probability and predicted classification
Feature importance ranking from the trained model
Fraud vs normal segmentation plot
Power BI dashboard for exploring fraud patterns
