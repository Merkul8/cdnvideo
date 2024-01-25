from cdnvideo.celery import app
from .services import get_all_cities
from .models import City

from math import radians, sin, cos, sqrt, atan2


@app.task
def get_two_cities(lat, lon):
    """ Задача celery для нахождения двух ближайших городов по
     заданным координатам """
    # Замена , на . если нужно
    lat = lat.replace(',', '.')
    lon = lon.replace(',', '.')
    # Конвертация прешедших данных в float
    lat = float(lat)
    lon = float(lon)
    lat_rad = radians(lat)
    lon_rad = radians(lon)

    cities = get_all_cities(City)
    distances = []

    for city in cities:
        # Преобразование координат в радианы
        city_lat = radians(city.latitude)
        city_lon = radians(city.longitude)

        # Формула Хаверсинуса 
        dlon = lon_rad - city_lon
        dlat = lat_rad - city_lat
        a = sin(dlat/2)**2 + cos(lat_rad) * cos(city_lat) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = 6371 * c # Радиус в километрах
        distances.append((distance, city))

    # Сортировка по дистанции
    distances.sort()

    # Берем первые два города
    closest_cities = [city for _, city in distances[:2]]
    return closest_cities