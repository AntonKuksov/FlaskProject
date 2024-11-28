from model.forecast import Forecast


def get_forecast_from_json(json) -> Forecast:
    new_forecast = Forecast(
        city=json['name'],
        units=True,
        humidity=json['main']['humidity'],
        wind_speed=json['wind']['speed'],
        current_temperature=json['main']['temp'],
        weather_description=json['weather'][0]['description']
    )
    return new_forecast
