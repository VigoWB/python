FROM python:3.13-alpine

#Ustawienia środowiskowe (wyłączenie plików .pyc, logi na STDOUT)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#Katalog roboczy wewnątrz kontenera
WORKDIR /app

# Instalacja zależności
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Kopiowanie całego projektu
COPY app .

# Wystawienie portu (ten sam, którego użyje runserver lub Gunicorn)
EXPOSE 5001

# Domyślne polecenie – dev-server Django
# Do produkcji zastąp poniższe dwie linie Gunicornem
CMD ["gunicorn", "moj_projekt.wsgi:application", "--bind", "0.0.0.0:5001"]