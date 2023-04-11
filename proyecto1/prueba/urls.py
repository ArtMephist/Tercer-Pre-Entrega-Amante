from django.urls import path
from prueba import views

urlpatterns = [
    path("Search/", views.BusquedaDatos, name="Search"),
    path("Registro/", views.register, name="Registro"),
    path("Inicio/", views.respuesta, name="Inicio")


]
