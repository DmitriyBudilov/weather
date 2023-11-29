from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias

from coordinates import Coordinates

URL = 'https://ipinfo.io/loc'

Celsius: TypeAlias = int

class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """Получить погодные данные из OpenWeather API."""
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2023-05-04 04:00:00"),
        sunset=datetime.fromisoformat("2023-05-04 20:30:00"),
        city="Moscow"
    )

if __name__ == '__main__':
    print(WeatherType.RAIN.value)