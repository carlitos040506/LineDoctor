from django.urls import path
from asistencia import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Bienvenidos/', views.bienvenidos, name = "bienvenidos")
]
    
