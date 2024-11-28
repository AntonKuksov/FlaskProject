import os

from model.forecast import Units


class Config:
    DEFAULT_CITY = os.getenv('DEFAULT_CITY', 'Tallinn')
    DEFAULT_UNITS = os.getenv('DEFAULT_UNITS', Units.METRIC.value)
    API_KEY = os.getenv('API_KEY', '44b04c5c9801970e82bb155d508f5666')
    API_URL = os.getenv('API_URL', 'http://api.openweathermap.org/data/2.5/weather')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key'.encode('utf8'))
    error = {
        "is_empty": "You were entering empty spaces. Please insert name of city",
        "is_number": "You entered a number instead of the city name. Please insert name of city",
        "wrong_default_city": "You entered an incorrect city name, please enter the name correctly in Settings.",
    }