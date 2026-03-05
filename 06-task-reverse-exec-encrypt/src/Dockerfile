FROM python:3.9-slim

RUN apt-get update && apt-get install -y gcc

RUN pip install pycryptodome

WORKDIR /src
COPY generate.py .

CMD ["python", "generate.py"]
