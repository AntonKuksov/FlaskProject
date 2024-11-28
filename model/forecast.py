from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Units(Enum):
    METRIC = "metric"
    IMPERIAL = "imperial"


@dataclass
class Forecast:
    city: str
    units: Units
    current_temperature: float
    weather_description: str
    humidity: Optional[float] = None
    wind_speed: Optional[float] = None
