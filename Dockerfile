FROM python:3.12-slim

WORKDIR /app

COPY job.py .
COPY test_addition.py .

CMD ["python3", "job.py"]
