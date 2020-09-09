from django.conf.urls import url 
from leaflet import views 
from django.urls import path

urlpatterns = [
    path('', views.index),
]