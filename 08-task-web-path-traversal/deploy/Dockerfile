FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src/ .

# Copy flag to root
COPY ./flag /flag

# Set permissions
RUN chown root:root /flag && chmod 644 /flag

# Expose port
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]
