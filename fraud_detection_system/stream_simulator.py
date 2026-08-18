import pandas as pd
import time
from alert_handler import send_alert
import joblib

model = joblib.load('models/fraud_model.pkl')
scaler = joblib.load('models/scaler.pkl')

df = pd.read_csv('data/transaction_data.csv')
X = df.select_dtypes(include=['float64', 'int64']).dropna()

X_scaled = scaler.transform(X)

for i, row in enumerate(X_scaled):
    prediction = model.predict([row])
    transaction_id = df.iloc[i].get("TransactionID", i)
    if prediction[0] == -1:
        send_alert(transaction_id, "Anomaly detected")
    time.sleep(1)  