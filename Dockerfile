FROM python:3.9-slim

# Create non-root user for security
RUN useradd -m -u 1000 monitor

USER monitor

WORKDIR /app

# Copy requirements first for better caching
COPY --chown=monitor requirements.txt .
RUN pip install --user -r requirements.txt

# Copy application code
COPY --chown=monitor . .

# Create results folder so advanced_monitor.py uses /app/results inside Docker
RUN mkdir -p /app/results

# Run the monitor
CMD ["python", "advanced_monitor.py"]