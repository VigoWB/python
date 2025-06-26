import os

class Config:
    SECRET_KEY = os.environ.get('SEKRETNY_KLUCZ') or 'nigdy-nie-zgadniesz'