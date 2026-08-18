import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv('data/transaction_data.csv')

# Preprocess
X = df.select_dtypes(include=['float64', 'int64']).dropna()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X_scaled)

# Save model & scaler
joblib.dump(model, 'models/fraud_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("✅ Model and Scaler saved.")
