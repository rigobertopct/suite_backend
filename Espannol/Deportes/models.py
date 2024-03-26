from django.db import models


# Create your models here.

class Deporte(models.Model):
    nombre = models.CharField(max_length=150)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Disciplina(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre
