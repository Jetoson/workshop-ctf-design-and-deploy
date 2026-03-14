FROM python:3.9-slim
RUN apt-get update && apt-get install -y binutils
WORKDIR /app
COPY solve.py .
CMD ["python", "solve.py"]
