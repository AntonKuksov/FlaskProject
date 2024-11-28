from flask import Flask, render_template, request, session

from config.config import Config
from service.request import get_forecast
from utils.check_form import is_empty, is_number

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY


@app.route('/', methods=['POST', 'GET'])
def load():
    forecasts = []
    errors = []
    if request.method == 'POST':
        if not is_empty(request.form['cities']):
            return render_template("error.html", error=Config.error['is_empty'])
        elif not is_number(request.form['cities']):
            return render_template("error.html", error=Config.error['is_number'])
        else:
            session['units'] = str(request.form.get('units'))
            cities = request.form['cities']
            city_list = [city.strip() for city in cities.split(',')]
            for city in city_list:
                try:
                    forecast = get_forecast(city)
                    forecast.units = session['units']
                    forecasts.append(forecast)
                except RuntimeError as e:
                    errors.append(f"Error fetching weather for {city}: {e}")
                    return render_template("error.html", error=errors)
            return render_template("index.html", forecasts=forecasts)
    else:
        try:
            session['units'] = Config.DEFAULT_UNITS
            forecast = get_forecast(session.get('default_city', Config.DEFAULT_CITY))
            forecasts.append(forecast)
            return render_template("index.html", forecasts=forecasts)
        except RuntimeError:
            return render_template("error.html", error=Config.error['wrong_default_city'])


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        session['api_key'] = request.form.get('api_key', Config.API_KEY).strip() or Config.API_KEY
        session['default_city'] = request.form.get('default_city', Config.DEFAULT_CITY).strip() or Config.DEFAULT_CITY
    return render_template("settings.html", default_city=session.get('default_city', Config.DEFAULT_CITY), api_key=session.get('api_key', Config.API_KEY))


if __name__ == '__main__':
    app.run()
