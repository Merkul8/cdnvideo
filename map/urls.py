from django.urls import path
from .views import (
    CityListAPIView,
    CityDetailAPIView,
)


urlpatterns = [
    path('cities/', CityListAPIView.as_view(), name='cities'),
    path('city/<int:pk>', CityDetailAPIView.as_view(), name='city'),
]