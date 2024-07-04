from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Bienvenidos', views.Bienvenidos, name='Bienvenidos'),
]
    
