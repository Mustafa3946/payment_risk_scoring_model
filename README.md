# Late Bill Payment Risk Scoring (Mock ML Project)

This project demonstrates an end-to-end machine learning pipeline designed to predict the likelihood of a user missing a future bill payment. It simulates a high-impact use case relevant to FinTech applications, with deployment on AWS using Lambda and API Gateway.

---

## 🧠 Problem Statement

Flexible payment platforms need to assess risk in real time to provide smarter bill scheduling and credit decisions. This project predicts whether a user will miss an upcoming bill payment based on their historical behavior.

---

## 🔧 Tech Stack

- **Language:** Python 3.10
- **ML Framework:** scikit-learn, XGBoost
- **Infrastructure:** AWS Lambda, API Gateway, S3 (optional)
- **Deployment Automation:** AWS CLI, shell scripts (CI/CD-ready)
- **Monitoring (future scope):** CloudWatch for logs and alerts

---

## 📊 Features Used

- Days since last payment
- Average bill amount
- Number of missed payments in the last 90 days
- Bill frequency pattern
- Seasonality of bill dates

---

## ⚙️ Pipeline Overview

1. **Data Ingestion:** Synthetic CSV data for users and payments
2. **Feature Engineering:** Custom logic to extract temporal and behavioral patterns
3. **Model Training:** Trained a binary classifier using `RandomForestClassifier`
4. **Model Serialization:** Saved using `joblib` for AWS deployment
5. **Deployment:** Packaged as AWS Lambda function with `/predict` endpoint via API Gateway
6. **Testing:** Endpoint accepts JSON input and returns a risk score + decision

---

## 📦 API Usage

**Endpoint:** `POST /predict`

**Sample Input:**
```json
{
  "user_id": "U12345",
  "days_since_last_payment": 35,
  "avg_bill_amount": 120.75,
  "missed_payments_90d": 2,
  "bill_frequency": "monthly"
}
```
**Sample Output:**
```json
{
  "risk_score": 0.78,
  "prediction": "high_risk"
}
```
