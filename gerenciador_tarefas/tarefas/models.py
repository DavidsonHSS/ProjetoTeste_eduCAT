from django.db import models
from django.utils import timezone

class Tarefa(models.Model):
    CATEGORIA_CHOICES = (
        ('verificar', 'Verificar'),
        ('importante', 'Importante'),
        ('urgente', 'Urgente'),
    )
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default='verificar')
    criado_por = models.CharField(max_length=100, default="nome_de_usuario_padrao")
    alterado_por = models.CharField(max_length=100, default="nome_de_usuario_padrao")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
class Status(models.Model):
    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField()
    
    def __str__(self):
        return self.descricao
