from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели City """
    
    class Meta:
        model = City
        fields = '__all__'