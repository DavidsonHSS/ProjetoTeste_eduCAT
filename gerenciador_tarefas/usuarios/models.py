from django.db import models


class Usuario (models.Model): 
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    ativo = models.BooleanField(default="",)

    def __str__(self):
        return self.nome

    