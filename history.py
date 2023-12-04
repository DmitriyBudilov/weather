from typing import Protocol

from weather_api_service import Weather

class WeatherStorage(Protocol):
    """Интерфейс для сохранения истории запросов погодных данных."""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError
    
class PlainFileWeatherStorage:
    def save(self, weather: Weather) -> None:
        print("Рефлизация сщхранения погоды...")

def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Сохранить погодные данные в хранилище."""
    storage.save(weather)

"TODO: https://to.digital/typed-python/weather/interfaces.html"