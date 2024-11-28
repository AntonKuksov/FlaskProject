import pytest
from app import app
from unittest.mock import patch

from config.config import Config


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'
    with app.test_client() as client:
        with client.session_transaction() as session:
            session['default_city'] = Config.DEFAULT_CITY
            session['api_key'] = Config.API_KEY
        yield client


def test_load_page_get(client):
    response = client.get('/')
    assert response.status_code == 200


def test_load_page_post_empty_city(client):
    response = client.post('/', data={'city': ''})
    assert response.status_code == 200
    assert b"You were entering empty spaces" in response.data



def test_load_page_post_valid_city(client):
    with patch('service.request.get_forecast', return_value={'city': 'Tallinn',}):
        response = client.post('/', data={'city': 'Tallinn'})
        print(response.data)
        assert response.status_code == 200
        assert b">Tallinn" in response.data
