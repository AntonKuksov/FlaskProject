import requests
from flask import session
from requests import RequestException

from config.config import Config
from model.forecast import Forecast
from utils.json_utils import get_forecast_from_json


def get_forecast(city: str) -> Forecast | RequestException:
    if Config.DEFAULT_CITY != city:
        Config.DEFAULT_CITY = city
    return fetch_forecast(Config.DEFAULT_CITY)


def fetch_forecast(city: str) -> Forecast:
    try:
        params = {
            "q": city,
            "units": session.get('units', Config.DEFAULT_UNITS),
            "appid": Config.API_KEY,
        }
        response = requests.get(Config.API_URL, params=params)
        response.raise_for_status()
        return get_forecast_from_json(response.json())
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching forecast for '{city}': {e}")