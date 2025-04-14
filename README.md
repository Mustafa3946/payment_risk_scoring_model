# Payment Risk Scoring Model

This project demonstrates the development of a payment risk scoring model using machine learning. The goal is to predict whether a user will make a late payment based on historical bill payment data and user-specific features.

The project is divided into the following main sections:
1. **Data Preparation** (`01_data_prep.ipynb`): Creating a synthetic dataset for training.
2. **Feature Engineering** (`02_feature_engineering.ipynb`): Transforming raw data into features suitable for model training.
3. **Model Training** (`03_model_training.ipynb`): Training a machine learning model to predict late payments.
4. **Lambda Packaging** (`04_lambda_packaging.ipynb`): Packaging the model for deployment on AWS Lambda.

## Setup Instructions

### Prerequisites
- Python 3.x
- Anaconda (for managing dependencies)
- AWS account (for SageMaker and Lambda deployment)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Mustafa3946/payment_risk_scoring_model.git
    cd payment_risk_scoring_model
    ```

2. Create and activate a conda environment:
    ```bash
    conda create --name payment_risk_scoring python=3.10
    conda activate payment_risk_scoring
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Notebooks Overview
1. **`01_data_prep.ipynb`**: 
   - Generates synthetic data for bill payments, including features like `bill_amount`, `days_late`, `user_avg_bill_amount`, etc.
   - Randomly simulates late and on-time payments.
   
2. **`02_feature_engineering.ipynb`**:
   - Applies transformations like encoding categorical variables and scaling continuous variables.
   - Features engineered for the model include `days_before_due_paid`, `user_avg_bill_amount`, and `user_late_payment_rate`.

3. **`03_model_training.ipynb`**:
   - Trains a random forest classifier using scikit-learn.
   - The model predicts whether a user will make a late payment based on historical features.

4. **`04_lambda_packaging.ipynb`**:
   - Packages the trained model and prediction function into a Lambda-compatible format for deployment.

## Features and Key Concepts

### Feature Engineering
In the **`02_feature_engineering.ipynb`**, we create the following features:
- `bill_amount`: The amount due for the bill.
- `days_late`: Whether the bill was paid late (0 if on time, 1 if late).
- `days_before_due_paid`: The number of days before the due date the bill was paid.
- `user_avg_bill_amount`: The average bill amount for the user over the last 6 months.
- `user_late_payment_rate`: The user's late payment rate over the last 6 months.
- `user_bill_count`: The number of bills the user has paid.

These features help the model learn patterns of user behavior and predict whether a user will pay a bill late in the future.

### Model Training
In **`03_model_training.ipynb`**, the following model training steps are performed:
- A Random Forest classifier is trained to predict the likelihood of a user making a late payment.
- The trained model is serialized using `joblib` for later use in predictions.

### Packaging for Deployment
In **`04_lambda_packaging.ipynb`**, the model is:
- Serialized into a format compatible with AWS Lambda.
- A Lambda function is created to allow real-time predictions for new data points.

## How to Use the Model

1. **Prepare Input Data**:
    Ensure the input dictionary follows the correct order of features as required by the trained model. The order should be:

    ```python
    ['bill_amount', 'days_late', 'days_before_due_paid', 'bill_month', 
     'bill_dayofweek', 'user_avg_bill_amount', 'user_late_payment_rate', 'user_bill_count']
    ```

2. **Make Predictions**:
    Once the model is trained, you can use the `predict_late_payment` function to make predictions based on the features.

    Example usage:

    ```python
    example = {
        'bill_amount': 230.5,
        'bill_month': 2,
        'bill_dayofweek': 4,
        'days_late': 0,
        'days_before_due_paid': 3,
        'user_avg_bill_amount': 210.2,
        'user_late_payment_rate': 0.2,
        'user_bill_count': 5
    }

    result = predict_late_payment(example)
    print(result)  # Output: 0 or 1 (0 for on-time, 1 for late)
    ```

## AWS Lambda Deployment
After training and testing the model locally, you can deploy it to AWS Lambda for real-time predictions.

1. **Package the Model**: The model and prediction function will be packaged into a Lambda-compatible format.
2. **Deploy to Lambda**: You can follow the provided steps in `04_lambda_packaging.ipynb` to deploy the function to AWS Lambda.

## Conclusion
This repository provides a fully working demonstration of building, training, and deploying a payment risk scoring model. It leverages machine learning techniques for predicting late payments based on user behavior and historical bill payment data.

Feel free to explore and extend the code for more advanced features or deployment in a production environment.
