from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('signup/', views.signup, name='registrar'),
    path('tarea/', views.tarea, name='tarea'),
    path('login/', views.inicioSesion, name='iniciosesion'),
    path('logout/', views.cerrarSesion, name='cerrar'),

]