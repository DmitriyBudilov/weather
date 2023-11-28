from urllib.request import urlopen

URL = 'https://ipinfo.io/loc'

def main(url: str) -> str:
    response = urlopen(URL)
    location = response.read()
    latitude, longitude = map(float, location.decode().strip().split(','))
    return latitude, longitude

if __name__ == '__main__':
    print(main(URL))