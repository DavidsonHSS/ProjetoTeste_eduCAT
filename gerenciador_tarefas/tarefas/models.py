from django.db import models

# Comandos / criar, atualizar, listar e excluir
# Precisa conter Titulo, descricao 
# Status / pendente, em andamento, concluido

class Tarefa (models.Model):

    CATEGORIA_CHOICES = (
        ('verificar', 'Verificar'),
        ('importante', 'Importante'),
        ('urgente', 'Urgente'),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default='verificar')
    
    def __str__(self):
        return self.titulo
    
class Status (models.Model):
    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField()
    
    def __str__(self):
        return self.descricao    
    
