from rest_framework import serializers
from .models import Tarefa, Status 

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'status', 'categoria']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','ativo', 'descricao']




        



