from django.db import models
# Create your models here.
from django.db.models import SET_NULL

from Espannol.Deportes.models import Disciplina, Deporte
from Espannol.nomencladores.models import Pais
from Espannol.seguridad.models import Provincia


class Deportista(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre y Apellidos", unique=True)
    edad = models.PositiveIntegerField(null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    estatura = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pais = models.ForeignKey(Pais, on_delete=SET_NULL, null=True, blank=True)
    sexo = models.CharField(max_length=25, null=True, blank=True)
    foto = models.ImageField(upload_to='pugiles', null=True, blank=True)
    ci = models.CharField(max_length=15, blank=True, null=True, unique=True)
    anno_deporte = models.IntegerField(blank=True, null=True)
    anno_nacional = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, null=True, blank=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def obtener_iniciales_y_digitos(self):
        deporte = self.deporte.siglas
        iniciales = ''.join([x[0].upper() for x in self.nombre.split()])
        ultimos_digitos = str(self.ci)[-5:]  # Obtener los últimos 5 dígitos del ID como texto
        return deporte + '-' + iniciales + ultimos_digitos

    def save(self, *args, **kwargs):
        if not self.codigo:  # Solo genera el código si no está definido ya
            self.codigo = self.obtener_iniciales_y_digitos()
        super(Deportista, self).save(*args, **kwargs)


class DeportistaDisciplina(models.Model):
    deportista = models.ForeignKey(Deportista, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
