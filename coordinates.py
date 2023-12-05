from dataclasses import dataclass
from subprocess import Popen, PIPE
from urllib.request import urlopen
from urllib.parse import urlparse

import config
from exceptions import CantGetCoordinates

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates(url: str) -> Coordinates:
    """Возвращает координаты устройства."""
    _check_url(url)
    coordinates = _get_device_coordinate(url)
    return _round_coordinates(coordinates)

def _check_url(url: str) -> bool:
    """Проверяет url адресс."""
    result = urlparse(url)
    if not all([result.scheme, result.netloc]):
        raise CantGetCoordinates
    return True

def _get_device_coordinate(url: str) -> Coordinates:
    """Получает координаты устройства."""
    # curl_output = _get_curl_output(url)
    curl_output = _get_location_output(url)
    coordinates = _parse_coordinates(curl_output)
    return coordinates

def _get_curl_output(url: str) -> bytes:
    """Отправляет запрос через утилиту «curl», возвращает bytes."""
    process = Popen(["curl", url], stdout=PIPE)
    output, err = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    return output

def _get_location_output(url: str) -> bytes:
    """Получает данные через urllib. Возвращает строку в bytes."""
    response = urlopen(url)
    if response.status != 200:
        raise CantGetCoordinates
    return response.read()

def _parse_coordinates(curl_output: bytes) -> Coordinates:
    """Парсит байтовую строку и возвращает Coordinate."""
    try:
        output = curl_output.decode().strip().split(',')
    except UnicodeDecodeError:
        raise CantGetCoordinates
    return _converte_coordinates(output)

def _converte_coordinates(output_line: list[str]) -> Coordinates:
    """Конвертирует координаты из str во float, возвращает Coordinate."""
    try:
        latitude, longitude = map(float, output_line)
    except ValueError:
        raise CantGetCoordinates
    return Coordinates(latitude, longitude)

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    """Округляет значения Coordinates."""
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
       lambda coordinate: round(coordinate, 1),
       [coordinates.latitude, coordinates.longitude] 
    ))


if __name__ == '__main__':
    location = get_gps_coordinates(config.COORDINATES_URL)
    print(location.latitude, location.longitude, sep='\n')
    # print(_check_url("https://ipinfo.io/loc"))
