import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("raw data/fraud_features.csv")

X = df[[
    "total_transactions",
    "total_spend",
    "avg_transaction_amount",
    "location_mismatch_count",
    "distinct_devices"
]]

y = df["fraud_events"] > 0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# Cross-validation to check model stability
cv_scores = cross_val_score(model, X, y, cv=5)
print("Cross Validation Accuracy:", cv_scores.mean())

# Predict probabilities instead of only class labels
probs = model.predict_proba(X_test)[:, 1]

# Lower fraud detection threshold
predictions = probs > 0.35

print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

importance = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importance:")
print(importance.sort_values(ascending=False))

# Apply model to entire dataset
df["fraud_probability"] = model.predict_proba(X)[:,1]
df["predicted_fraud"] = df["fraud_probability"] > 0.35

df.to_csv("fraud_predictions.csv", index=False)
print("Predictions exported to fraud_predictions.csv")

fraud = df[df["predicted_fraud"] == True]
normal = df[df["predicted_fraud"] == False]

plt.figure(figsize=(8,6))

plt.scatter(
    normal["total_spend"],
    normal["distinct_devices"],
    alpha=0.4,
    label="Normal Accounts"
)

plt.scatter(
    fraud["total_spend"],
    fraud["distinct_devices"],
    alpha=0.8,
    label="Fraud Accounts"
)

plt.xlabel("Total Spend")
plt.ylabel("Distinct Devices")
plt.title("Fraud Risk Segmentation")
plt.legend()

plt.tight_layout()
plt.savefig("fraud_risk_scatter.png")
