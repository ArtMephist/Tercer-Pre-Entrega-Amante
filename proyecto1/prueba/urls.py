from django.urls import path
from prueba import views

urlpatterns = [
    path("Search/", views.BusquedaDatos, name="Search"),
    path("register/", views.register, name="Register"),
    path("", views.respuesta)


]
