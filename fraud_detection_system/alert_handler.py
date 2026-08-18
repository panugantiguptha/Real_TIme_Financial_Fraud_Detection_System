def send_alert(transaction_id, reason):
    print(f"🚨 ALERT: Fraudulent transaction detected! ID: {transaction_id}, Reason: {reason}")
    # Extend to email, SMS, or Kafka queue in production
