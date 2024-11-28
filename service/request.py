import requests
from requests import RequestException

from config.config import Config
from model.forecast import Forecast
from utils.json_utils import get_forecast_from_json

url = Config.API_URL

def get_forecast(city:str) -> Forecast | RequestException:
    if Config.DEFAULT_CITY == city:
        try:
            response = requests.get(f"{url}?q={Config.DEFAULT_CITY}&units={Config.DEFAULT_UNITS}&appid={Config.API_KEY}")
            response.raise_for_status()
            data = response.json()
            return get_forecast_from_json(data)
        except requests.RequestException as e:
            return e
    else:
        try:
            Config.DEFAULT_CITY = city
            response = requests.get(f"{url}?q={Config.DEFAULT_CITY}&units={Config.DEFAULT_UNITS}&appid={Config.API_KEY}")
            response.raise_for_status()
            data = response.json()
            return get_forecast_from_json(data)
        except requests.RequestException as e:
            return e
