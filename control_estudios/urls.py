"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from control_estudios.views import listar_albums, eliminar_canciones, filtrar_albums, filtrar_canciones, eliminar_albums, buscar_albums, buscar_canciones, crear_canciones, crear_albums, listar_canciones, listar_artistas, crear_artistas, eliminar_artistas,\
    buscar_artistas


urlpatterns = [
    path("albums/", listar_albums, name="lista_albums"),
    path("artistas/", listar_artistas, name="lista_artistas"),
    path("canciones/", listar_canciones, name="lista_canciones"),
    path("crear-artistas/", crear_artistas, name="crear_artistas"),
    path("crear-albums/", crear_albums, name="crear_albums"),
    path("crear-canciones/", crear_canciones, name="crear_canciones"),
    path("eliminar-artistas/", eliminar_artistas, name="eliminar_artistas"),
    path("eliminar-albums/", eliminar_albums, name="eliminar_albums"),
    path("eliminar-canciones/", eliminar_canciones, name="eliminar_canciones"),
    path("buscar-artistas/", buscar_artistas, name="buscar_artistas"),
    path("buscar-albums/", buscar_albums, name="buscar_albums"),
    path("buscar-canciones/", buscar_canciones, name="buscar_canciones"),
    path("filtrar-canciones/", filtrar_canciones, name="filtrar_canciones"),
    path("filtrar-albums/", filtrar_albums, name="filtrar_albums")
]
