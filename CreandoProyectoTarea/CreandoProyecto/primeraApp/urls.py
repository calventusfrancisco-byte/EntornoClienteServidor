from django.urls import path
from . import views

urlpatterns = [
    path('', views.primeraApp),
    path('contacto', views.contacto),
    path('calendario', views.calendario),
    path('tresEnRaya', views.tresEnRaya, name= '3EnRaya')
]