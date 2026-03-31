## Fraud Pattern Detection Pipeline

### Description
This project reviews transaction behavior to flag accounts showing patterns commonly associated with fraud. Raw transaction data is cleaned and shaped into account-level behavioral features, then used to train a Random Forest classifier that scores fraud risk. The goal is not just to label suspicious accounts, but to produce a usable risk signal that can be reviewed alongside spending behavior and device activity.

### Stack
- Python
- scikit-learn
- pandas
- matplotlib
- Power BI

### Pipeline
1. Raw transaction data is grouped and transformed into account-level behavioral features.
2. The feature set is loaded into Python for model training and evaluation.
3. A Random Forest classifier is trained to separate likely fraudulent accounts from normal accounts.
4. Class imbalance is handled using balanced class weights.
5. Model performance is reviewed using classification metrics and a confusion matrix.
6. Fraud probabilities are generated and exported for downstream analysis and reporting.

### Model Features
- `total_transactions`
- `total_spend`
- `avg_transaction_amount`
- `location_mismatch_count`
- `distinct_devices`

### Outputs
- `fraud_predictions.csv` containing fraud probability and predicted fraud classification for each account
- Feature importance ranking from the trained model
- Fraud vs normal segmentation plot
- Power BI dashboard for reviewing fraud patterns, account behavior, and model output
