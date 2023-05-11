from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_estudios.forms import CancionesFormulario, ArtistasFormulario, AlbumsFormulario
from control_estudios.models import Canciones, Albums, Artistas

""""
def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response
"""

def listar_artistas(request):
    contexto = {
        "artistas": Artistas.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_artistas.html',
        context=contexto,
    )
    return http_response

def listar_albums(request):
    contexto = {
        "albums": Albums.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_albums.html',
        context=contexto,
    )
    return http_response


def listar_canciones(request):
    contexto = {
        "canciones": Canciones.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_canciones.html',
        context=contexto,
    )
    return http_response
""""
def crear_curso_version_1(request):
    No la estamos usando
    if request.method == "POST":
        data = request.POST  # es un diccionario
        nombre = data["nombre"]
        comision = data["comision"]
        curso = Curso(nombre=nombre, comision=comision)  # lo crean solo en RAM
        curso.save()  # Lo guardan en la Base de datos

        # Redirecciono al usuario a la lista de cursos
        url_exitosa = reverse('lista_cursos')  # estudios/cursos/
        return redirect(url_exitosa)
    else:  # GET
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_curso_a_mano.html',
        )
        return http_response
"""

def crear_artistas(request):
    if request.method == "POST":
        formulario = ArtistasFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            apellido = data["apellido"]
            artistas = Artistas(nombre=nombre, apellido=apellido)  # lo crean solo en RAM
            artistas.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_artistas')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ArtistasFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_artistas.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_albums(request):
    if request.method == "POST":
        formulario = AlbumsFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            nombre_artista = data["nombre_artista"]
            albums = Albums(nombre=nombre, nombre_artista=nombre_artista)  # lo crean solo en RAM
            albums.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_albums')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = AlbumsFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_albums.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_canciones(request):
    if request.method == "POST":
        formulario = CancionesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            nombre_album = data["nombre_album"]
            albums = Canciones(nombre=nombre, nombre_album=nombre_album)  # lo crean solo en RAM
            albums.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_canciones')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = CancionesFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_canciones.html',
        context={'formulario': formulario}
    )
    return http_response


def eliminar_artistas(request):
    if request.method == 'POST':
        artistas_id = request.POST.getlist('artistas_id')
        artistas = Artistas.objects.filter(id__in=artistas_id)
        artistas.delete()
        return redirect('lista_artistas')
    
    artistas = Artistas.objects.all()
    contexto = {
        "artistas": artistas,
    }
    http_response = render(
        request=request,
        template_name='control_estudios/eliminar_artistas.html',
        context=contexto
    )
    return http_response
    

def eliminar_albums(request):
    if request.method == 'POST':
        albums_id = request.POST.getlist('albums_id')
        albums = Albums.objects.filter(id__in=albums_id)
        albums.delete()
        return redirect('lista_albums')
    
    albums = Albums.objects.all()
    contexto = {
        "albums": albums,
    }
    http_response = render(
        request=request,
        template_name='control_estudios/eliminar_albums.html',
        context=contexto
    )
    return http_response
    

def eliminar_canciones(request):
    if request.method == 'POST':
        canciones_id = request.POST.getlist('canciones_id')
        canciones = Canciones.objects.filter(id__in=canciones_id)
        canciones.delete()
        return redirect('lista_canciones')
    
    canciones = Canciones.objects.all()
    contexto = {
        "canciones": canciones,
    }
    http_response = render(
        request=request,
        template_name='control_estudios/eliminar_canciones.html',
        context=contexto
    )
    return http_response
    


def buscar_artistas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        artistas = Artistas.objects.filter(Q(nombre__contains=busqueda) | Q(apellido__contains=busqueda))
        contexto = {
            "artistas": artistas,
            "reciente": busqueda
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_artistas.html',
            context=contexto,
        )
        return http_response

def buscar_albums(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        albums = Albums.objects.filter(nombre__contains=busqueda)
        contexto = {
            "albums": albums,
            "reciente": busqueda
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_albums.html',
            context=contexto,
        )
        return http_response
    
def buscar_canciones(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        canciones = Canciones.objects.filter(nombre__contains=busqueda)
        contexto = {
            "canciones": canciones,
            "reciente": busqueda
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_canciones.html',
            context=contexto,
        )
        return http_response