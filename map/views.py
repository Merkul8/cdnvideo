from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CitySerializer
from .models import City
from .services import get_all_cities
from .tasks import get_two_cities


class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = get_all_cities(City)


class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = get_all_cities(City)


class City2CityAPIView(APIView):
    """ Представление для нахождения двух ближайших городов
     по заданным координатам """

    def get(self, request, lat, lon):
        # Задача celery, get_two_cities - функция для поиска ближайших городов
        task = get_two_cities.delay(lat, lon)
        result = task.get(timeout=10)

        serializer = CitySerializer(result, many=True)
        return Response({'cities': serializer.data, 'status': 200})


