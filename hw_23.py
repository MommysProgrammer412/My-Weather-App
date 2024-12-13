from urllib import response
import requests
from plyer import notification

API_KEY = r'b7a99c8304c6cb7c05b09085adceea09'
CITY = 'Ханты-Мансийск'

def get_weather(city: str, api_key: str) -> dict:
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()