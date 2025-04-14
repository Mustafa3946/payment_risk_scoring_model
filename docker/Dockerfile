FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy code and model
COPY app/inference.py ./inference.py
COPY model/model_rf.joblib ./model.joblib
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app (for testing locally)
CMD ["python", "inference.py"]
