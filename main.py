import requests
import datetime

url_coords = 'http://search.maps.sputnik.ru/search/addr?'
url_weather = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?'
api_weather = '947a8a6c011298e5751700b3bf942c8f'
time = (datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0) - datetime.timedelta(days=4)).timestamp()
timedelta = datetime.timedelta(days=1)

city = input()

response = requests.get(
    url_coords,
    params={'q': city},
)
coords = response.json()['result']['address'][0]['features'][0]['geometry']['geometries'][0]['coordinates']

for _ in range(5):
    response = requests.get(
        url_weather,
        params={'lat': coords[1], 'lon': coords[0], 'dt': int(time), 'appid': api_weather}
    )
    temperature = response.json()
    print(datetime.datetime.fromtimestamp(temperature['current']['dt']).strftime('%d.%m.%Y') + ':',
          str(round(temperature['current']['temp'] - 273.15, 1)) + '°C')
    time = (datetime.datetime.fromtimestamp(time) + timedelta).timestamp()

