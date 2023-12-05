COORDINATES_URL = 'https://ipinfo.io/loc' # Ресурс возвращающий данные об устройстве запроса.
USE_ROUNDED_COORDS = True # Флаг округления значения координат.
OPENWEATHER_API_KEY = "7549b3ff11a7b2f3cd25b56d21c83c6a" # Ключ для API-запросов к openwether.
# Конструктор URL-запроса к openweather.
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API_KEY + "&lang=ru&"
    "units=metric"
)