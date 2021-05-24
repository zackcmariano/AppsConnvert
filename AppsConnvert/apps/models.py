from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.nome