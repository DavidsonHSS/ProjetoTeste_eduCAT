from django.shortcuts import render
from django.http import JsonResponse
from .models import Tarefa, Status
from .serializers import TarefaSerializer, StatusSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

def lista_tarefas_list(request):
    lista_tarefas = Tarefa.objects.filter(status='pendente')
    return render(request, 'tarefas/lista_tarefas.html', {'lista_tarefas': lista_tarefas})


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
