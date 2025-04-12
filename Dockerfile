# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy source code
COPY app/ ./app/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "-m", "app.main"]
