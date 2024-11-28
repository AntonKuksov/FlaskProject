import pytest
from app import app
from unittest.mock import patch

from config.config import Config
from model.forecast import Forecast, Units


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'
    with app.test_client() as client:
        with client.session_transaction() as session:
            session['default_city'] = Config.DEFAULT_CITY
            session['api_key'] = Config.API_KEY
        yield client

def mock_forecast():
    return Forecast(
        city="Tallinn",
        units=Units.METRIC,
        current_temperature=5.0,
        weather_description="Clear sky",
        humidity=80,
        wind_speed=5.5
    )

def test_load_page_get(client):
    response = client.get('/')
    assert response.status_code == 200


def test_post_empty_city(client):
    response = client.post('/', data={'city': ''})
    assert response.status_code == 200
    assert b"empty spaces" in response.data


def test_post_valid_city(client):
    with patch('service.request.get_forecast', return_value=mock_forecast()):
        response = client.post('/', data={'city': 'Tallinn'})
        assert response.status_code == 200
        assert b"Tallinn" in response.data