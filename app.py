from flask import Flask, render_template, request, session

from config.config import Config
from service.request import get_forecast
from utils.check_form import is_empty, is_number

app = Flask(__name__)
app.secret_key = 'your_secret_key'.encode('utf8')


error = {
  "is_empty": "You were entering empty spaces. Please insert name of city",
  "is_number": "You entered a number instead of the city name. Please insert name of city",
}
@app.route('/', methods=['POST', 'GET'])
def load():
    if request.method == 'POST':
        if not is_empty(request.form['city']):
            return render_template("error.html", error=error['is_empty'])
        elif not is_number(request.form['city']):
            return render_template("error.html", error=error['is_number'])
        else:
            set_units(str(request.form.get('units')))
            forecast_data = get_forecast(request.form['city'])
            forecast_data.units = set_units(str(request.form.get('units')))
            if isinstance(forecast_data, str):
                return render_template("error.html", error=forecast_data)
            else:
                return render_template("index.html", forecast=forecast_data)
    else:
        Config.API_KEY = session['api_key']
        forecast_data = get_forecast(session.get('default_city', Config.DEFAULT_CITY))
        return render_template("index.html", forecast=forecast_data)

def set_units(select_value)-> bool:
    match select_value:
        case "1":
            Config.DEFAULT_UNITS = "metric"
            return True
        case "2":
            Config.DEFAULT_UNITS = "imperial"
            return False



@app.route('/settings', methods=['POST', 'GET'])
def settings():
    default_city = session.get('default_city', Config.DEFAULT_CITY)
    api_key = session.get('api_key', Config.API_KEY)
    if request.method == 'POST':
        api_key = request.form.get('api_key', api_key)
        session['api_key'] = api_key
        default_city = request.form.get('default_city', default_city)
        session['default_city'] = default_city

    return render_template("settings.html", default_city=default_city, api_key=api_key)

if __name__ == '__main__':
    app.run()
