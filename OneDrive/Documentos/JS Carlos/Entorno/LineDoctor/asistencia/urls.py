from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('paginas/nosotros/', views.nosotros, name='nosotros'),
    path('estudiantes/crear/', views.crear, name='crear'),
    path('estudiantes/editar/', views.editar, name='editar'),
    path('estudiantes/index/', views.index, name='index'),
    path('paginas/registro/', views.registro, name='registro'),
    path('paginas/login/', views.login, name='login'),
    path('estudiantes/publicaciones/', views.publicaciones, name='publicaciones'),
    path('paginas/olvidocontraseña/', views.olvidocontraseña, name='olvidocontraseña'),
]