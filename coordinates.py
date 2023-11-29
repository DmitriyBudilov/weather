from dataclasses import dataclass
from subprocess import Popen, PIPE
from urllib.request import urlopen

from exceptions import CantGetCoordinates

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates(url: str) -> Coordinates:
    """Вернуть координаты устройства."""
    process = Popen(["curl", url], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    output_line = output.decode().strip().split(',')
    # try:
    #     response = urlopen(url)
    # except Exception as error:
    #     raise CantGetCoordinates
    # location = response.read()
    latitude, longitude = map(float, output_line)
    return Coordinates(latitude=latitude, longitude=longitude)

if __name__ == '__main__':
    location = get_gps_coordinates('https://ipinfo.io/loc')
    print(location.latitude, location.longitude, sep='\n')