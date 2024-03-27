from django.db import models
# Create your models here.
from django.db.models import PROTECT

from Espannol.deportista.models import Deportista
from Espannol.nomencladores.models import Evento
from Espannol.seguridad.models import ExtendUser


class Categoria(models.Model):
    categoria = models.CharField(max_length=255, verbose_name="Categoría", unique=True)
    peso_min = models.DecimalField(max_digits=5, decimal_places=2)
    peso_max = models.DecimalField(max_digits=5, decimal_places=2)
    idioma = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'


class Pugil(models.Model):
    deportista = models.ForeignKey(Deportista, on_delete=PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=PROTECT)
    ranking = models.CharField(max_length=10)

    def __str__(self):
        return self.deportista.nombre


class Combate(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    esquinaR = models.ForeignKey(Pugil, on_delete=models.PROTECT, related_name='person1', null=True, blank=True)
    esquinaA = models.ForeignKey(Pugil, on_delete=models.PROTECT, related_name='person', null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return self.esquinaA.deportista.nombre + ' vs ' + self.esquinaR.deportista.nombre + ' en ' + self.evento.nombre

    class Meta:
        verbose_name = 'combate'
        verbose_name_plural = 'combates'
        db_table = 'combate'


class CodifResultado(models.Model):
    resul = models.CharField(max_length=255, verbose_name="resultado")
    descripcion = models.CharField(max_length=255, verbose_name="descripción")
    idioma = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.resul

    class Meta:
        verbose_name = 'codifresultado'
        verbose_name_plural = 'codifresultados'
        db_table = 'codifresultado'


class Resultado(models.Model):
    combate = models.ForeignKey(Combate, on_delete=models.SET_NULL, null=True, blank=True)
    pugil = models.ForeignKey(Pugil, on_delete=models.SET_NULL, null=True, blank=True)
    resultado = models.ForeignKey(CodifResultado, on_delete=models.SET_NULL, null=True, blank=True)
    idioma = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.pugil.deportista.nombre + ' ' + self.resultado.resul + ' en ' + self.combate.evento.nombre

    class Meta:
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'
        db_table = 'resultado'


class Golpe(models.Model):
    golpe = models.CharField(max_length=255, verbose_name="golpe")
    siglas = models.CharField(max_length=10, verbose_name="siglas", null=True, blank=True)
    efectivo = models.BooleanField(default=False, null=True, blank=True)
    idioma = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.golpe

    class Meta:
        verbose_name = 'golpe'
        verbose_name_plural = 'golpes'
        db_table = 'golpe'


class ContadorGolpes(models.Model):
    combate = models.ForeignKey(Combate, on_delete=models.SET_NULL, null=True, blank=True)
    numero_asalto = models.PositiveIntegerField()
    golpe = models.ForeignKey(Golpe, on_delete=models.SET_NULL, null=True, blank=True)
    esquina = models.ForeignKey(Pugil, on_delete=models.SET_NULL, verbose_name="esquina", null=True, blank=True)
    tiempo = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.esquina.deportista.nombre + '-' + self.golpe.siglas

    class Meta:
        verbose_name = 'contadorgolpe'
        verbose_name_plural = 'contadorgolpes'
        db_table = 'contador_golpe'


class ConfigGolpe(models.Model):
    user = models.ForeignKey(ExtendUser, on_delete=models.SET_NULL, null=True, blank=True)
    golpe = models.ForeignKey(Golpe, on_delete=models.SET_NULL, null=True, blank=True)
    tecla = models.CharField(max_length=255, verbose_name="tecla")
    idioma = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.user.username + '-' + self.golpe.siglas + '-' + self.tecla

    class Meta:
        verbose_name = 'configolpe'
        verbose_name_plural = 'configolpes'
        db_table = 'config_golpe'
