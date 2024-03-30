from django.contrib import admin
from .models import Tarefa, Status

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass