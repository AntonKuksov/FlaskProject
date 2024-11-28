from dataclasses import dataclass
from typing import Optional


@dataclass
class Forecast:
    city: str
    units: bool
    current_temperature: float
    weather_description: str
    humidity: Optional[float] = None
    wind_speed: Optional[float] = None
