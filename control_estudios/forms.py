from django import forms


class ArtistasFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    apellido = forms.CharField(required=False, max_length=64) 

class AlbumsFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    nombre_artista = forms.CharField(required=True, max_length=64)

class CancionesFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    nombre_album = forms.CharField(required=True, max_length=64)