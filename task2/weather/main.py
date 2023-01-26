import requests
from datetime import timedelta, datetime
from django.utils import dateparse


key = 'a69041bbf8b768cd7c8bac08a6087b49'


def add_city(city):
    r = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}'
    )
    city_info = r.json()
    if not city_info:
        return []

    'Находим координаты города'
    lat = city_info[0]['lat']
    lon = city_info[0]['lon']

    r2 = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}'
    )
    weather = r2.json()
    result = {
        'city': weather["name"],
        'temperature': weather["main"]["temp"],
        'atmosphere_pressure': weather["main"]["pressure"] * 0.75,
        'wind_speed': weather["wind"]["speed"],
    }
    return result


def update_check_time(date, interval=30):
    """Функция проверки даты обновления,
    первым аргументом принимает дату из модели(DateTimeField),
    второй аргумент время интервала в минутах,
    возвращает булевое значение(если обновление было меньше "interval",
    то возвращает True)."""
    d = dateparse.parse_datetime(str(date))
    normalize_date = datetime(
        d.year, d.month, d.day, d.hour, d.minute, d.second
    )
    now = datetime.now()
    period = now - timedelta(minutes=interval)
    return normalize_date > period
