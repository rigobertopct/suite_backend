from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
from django.db.models import PROTECT


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class ExtendUser(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=PROTECT, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username
