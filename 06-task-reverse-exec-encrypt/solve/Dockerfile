FROM python:3.9-slim
RUN apt-get update && apt-get install -y binutils
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY solve.py .
CMD ["python", "solve.py"]
