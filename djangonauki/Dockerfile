FROM python:3.13-slim

# Ustawienia środowiskowe - brak .pyc, natychmiastowe logi
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Skopiuj requirements i zainstaluj zależności
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Skopiuj cały kod projektu
COPY . .

EXPOSE 8000

# Domyślne polecenie - w produkcji użyj gunicorn!
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]