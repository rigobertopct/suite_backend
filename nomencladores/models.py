from django.db import models


# Create your models here.


class TipoEvento(models.Model):
    tipo = models.CharField(max_length=250, verbose_name="Tipo de Evento")
    idioma = models.CharField(max_length=255, verbose_name="Idioma", default="es")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'tipo_evento'
        verbose_name_plural = 'tipo_eventos'
        db_table = 'tipo_evento'


class Pais(models.Model):
    pais = models.CharField(max_length=250, verbose_name="País")
    siglas = models.CharField(max_length=250, verbose_name="Siglas")

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        db_table = 'pais'


class Reglamento(models.Model):
    tipo = models.CharField(max_length=255, verbose_name="Reglamento", unique=True)
    cant_r = models.IntegerField(verbose_name="Cantidad de round")
    duracion = models.IntegerField(verbose_name="Duración")
    idioma = models.CharField(max_length=255, verbose_name="Idioma", default="es")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'reglamento'
        verbose_name_plural = 'reglamentos'
        db_table = 'reglamento'


class Evento(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Evento", unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    tipoevento = models.ForeignKey(TipoEvento, on_delete=models.SET_NULL, null=True, blank=True)
    anno = models.PositiveIntegerField(verbose_name="Año")
    reglamento = models.ForeignKey(Reglamento, on_delete=models.SET_NULL, null=True, blank=True)
    idioma = models.CharField(max_length=255, verbose_name="Idioma", default="es")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        db_table = 'evento'
