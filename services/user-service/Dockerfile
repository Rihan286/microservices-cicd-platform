# Stage 1: Build dependencies
FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Runtime image
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]