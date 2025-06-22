FROM python:3.13-alpine

WORKDIR /app

# Copy and install all pip requirements
COPY assets/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV="docker"

EXPOSE 5000


