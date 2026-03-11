import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

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

model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))
importance = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importance:")
print(importance.sort_values(ascending=False))
df["predicted_fraud"] = model.predict(X)
df.to_csv("fraud_predictions.csv", index=False)
print("Predictions exported to fraud_predictions.csv")
import matplotlib.pyplot as plt

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