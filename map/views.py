from rest_framework import generics
from .serializers import CitySerializer
from .models import City


class CityListAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

