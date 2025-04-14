import joblib
import pandas as pd

model = joblib.load('model.joblib')

def predict(input_dict):
    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)
    return int(prediction[0])

if __name__ == "__main__":
    sample = {
        'bill_amount': 230.5,
        'days_late': 0,
        'days_before_due_paid': 3,
        'bill_month': 2,
        'bill_dayofweek': 4,
        'user_avg_bill_amount': 210.2,
        'user_late_payment_rate': 0.2,
        'user_bill_count': 5
    }

    result = predict(sample)
    print(f"Predicted Late: {result}")
