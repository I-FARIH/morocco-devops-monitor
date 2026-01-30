# Dockerfile for Moroccan Website Monitor
FROM python:3.9-alpine

WORKDIR /app

# Create directory for results
RUN mkdir -p /app/results

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY website_checker.py .

# Create non-root user for security
RUN adduser -D -u 1000 appuser
RUN chown -R appuser:appuser /app
USER appuser

# Run the monitoring script
CMD ["python", "./website_checker.py"]
