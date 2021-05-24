from django.shortcuts import render
from rest_framework import viewsets
from apps.models import Usuario
from apps.serializer import UsuarioSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# Create your views here.
def home(request):
    return render(request, 'index.html')

def api(request):
   return render(request, 'api.html')

def apidjangorest(request):
    return render(request, 'djangorest.html')