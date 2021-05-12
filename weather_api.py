import requests
import datetime
import os


appid = os.environ.get('OPEN_WEATHER_API_KEY')

def check_city_name(city: str):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather',
                     params={'q': city, 'appid': appid, 'units': 'metric'})
    return True if r.ok else False

def get_weather(city: str, id: int):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather',
                     params={'q': city, 'appid': appid, 'units': 'metric'})
    if not r.ok:
        return None
    current_time = (datetime.datetime.utcnow() + datetime.timedelta(seconds=r.json()['timezone'])).hour
    card_type = 'card day'
    if 4 < current_time <= 6:
        card_type = 'card evening-morning'
    elif current_time > 19 or current_time <= 4:
        card_type = 'card night'
    return {
        'id': id,
        'city_name': city,
        'temp': r.json()['main']['temp'],
        'state': r.json()['weather'][0]['main'],
        'card_type': card_type
    }
