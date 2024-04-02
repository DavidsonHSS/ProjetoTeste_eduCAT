from django.shortcuts import render
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets, response 


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer