from django.urls import path
from . import views


urlpatterns = [
    path('cities/', views.CityListAPIView.as_view(), name='cities'),
    path('city/<int:pk>', views.CityDetailAPIView.as_view(), name='city'),
    path('cities/<str:lat>/<str:lon>/', views.City2CityAPIView.as_view(), name='nearest_cities'),
]