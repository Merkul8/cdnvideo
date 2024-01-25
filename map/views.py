from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CitySerializer
from .services import get_all_cities
from .tasks import get_two_cities


class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = get_all_cities()


class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = get_all_cities()


class City2CityAPIView(APIView):
    """ Представление для нахождения двух ближайших городов
     по заданным координатам """

    def get(self, request, lat, lon):
        # get_two_cities - функция нахождения двух ближайших городов
        serializer = CitySerializer(get_two_cities.delay(lat, lon), many=True)
        return Response({'cities': serializer.data, 'status': 200})


