import logging
import time

import requests
from flask import session
from requests import RequestException

from config.config import Config
from model.forecast import Forecast
from utils.json_utils import get_forecast_from_json

logging.basicConfig(level=logging.DEBUG)

cache = {}
CACHE_TIMEOUT = 300


def get_forecast(city: str) -> Forecast | RequestException:
    if Config.DEFAULT_CITY != city:
        Config.DEFAULT_CITY = city
    units = session.get('units', Config.DEFAULT_UNITS)
    cached_data = get_cached_forecast(city, units)
    if cached_data:
        logging.info(f"Take it from cache: {city}")
        return cached_data

    forecast = fetch_forecast(Config.DEFAULT_CITY, units)
    cache_forecast(city, units, forecast)
    logging.info(f"Take it from API: {city}")
    return forecast


def fetch_forecast(city: str,units: str) -> Forecast:
    try:
        params = {
            "q": city,
            "units": units,
            "appid": Config.API_KEY,
        }
        response = requests.get(Config.API_URL, params=params)
        response.raise_for_status()
        return get_forecast_from_json(response.json())
    except requests.RequestException as e:
        logging.error(f"Error fetching forecast for '{city}': {e}")
        raise RuntimeError(f"Error fetching forecast for '{city}': {e}")


def get_cached_forecast(city: str, units: str) -> Forecast | None:
    key = (city, units)
    cached_entry = cache.get(key)
    if cached_entry:
        timestamp, forecast = cached_entry
        if time.time() - timestamp < CACHE_TIMEOUT:
            logging.info(f"Using cached forecast for '{city}'")
            return forecast
        else:
            logging.info(f"Cache expired for '{city}'")
            cache.pop(city)
    return None


def cache_forecast(city: str, units: str, forecast: Forecast):
    key = (city, units)
    cache[key] = (time.time(), forecast)
    logging.info(f"Cached forecast for '{city}'")