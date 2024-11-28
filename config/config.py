import os


class Config:
    DEFAULT_CITY = os.getenv('DEFAULT_CITY', 'Tallinn')
    DEFAULT_UNITS = os.getenv('DEFAULT_UNITS', 'metric')
    API_KEY = os.getenv('API_KEY', '44b04c5c9801970e82bb155d508f5666')
    API_URL = os.getenv('API_URL', 'http://api.openweathermap.org/data/2.5/weather')
