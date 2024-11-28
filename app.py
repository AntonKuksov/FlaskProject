from flask import Flask, render_template, request, session

from config.config import Config
from service.request import get_forecast
from utils.check_form import is_empty, is_number

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY


@app.route('/', methods=['POST', 'GET'])
def load():
    if request.method == 'POST':
        if not is_empty(request.form['city']):
            return render_template("error.html", error=Config.error['is_empty'])
        elif not is_number(request.form['city']):
            return render_template("error.html", error=Config.error['is_number'])
        else:
            try:
                session['units'] = str(request.form.get('units'))
                forecast_data = get_forecast(request.form['city'])
                forecast_data.units = session['units']
                return render_template("index.html", forecast=forecast_data)
            except RuntimeError:
                return render_template("error.html", error=Config.error['wrong_city'])
    else:
        try:
            session['units'] = Config.DEFAULT_UNITS
            forecast_data = get_forecast(session.get('default_city', Config.DEFAULT_CITY))
            return render_template("index.html", forecast=forecast_data)
        except RuntimeError:
            return render_template("error.html", error=Config.error['wrong_city'])


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        session['api_key'] = request.form.get('api_key', Config.API_KEY).strip() or Config.API_KEY
        session['default_city'] = request.form.get('default_city', Config.DEFAULT_CITY).strip() or Config.DEFAULT_CITY
    return render_template("settings.html", default_city=session.get('default_city', Config.DEFAULT_CITY), api_key=session.get('api_key', Config.API_KEY))


if __name__ == '__main__':
    app.run()
