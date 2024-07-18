from django.urls import path
<<<<<<< HEAD
from asistencia import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Bienvenidos/', views.bienvenidos, name = "bienvenidos")
=======
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Bienvenidos', views.Bienvenidos, name='Bienvenidos'),
>>>>>>> e63d76852051e20e929554978d47a01273c5b537
]
    
