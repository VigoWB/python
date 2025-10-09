FROM python:3.9.15-slim-bullseye

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

WORKDIR /app/mastermind

CMD ["python", "mastermind.py"]