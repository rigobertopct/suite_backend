from django.db import models

from deportista.models import Deportista
from seguridad.models import Provincia


class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    idioma = models.CharField(max_length=255, verbose_name="Idioma", default="es")

    def __str__(self):
        return self.nombre


class Prueba(models.Model):
    fecha = models.DateField()
    deportista = models.ForeignKey(Deportista, on_delete=models.PROTECT)
    lugar = models.ForeignKey(Lugar, on_delete=models.PROTECT)
    archivo = models.FileField(null=True, blank=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    etapa = models.CharField(max_length=255, null=True, blank=True)
    valoracion = models.CharField(max_length=255, null=True, blank=True)
    idioma = models.CharField(max_length=255, verbose_name="Idioma", default="es")

    class Meta:
        verbose_name = 'prueba'
        verbose_name_plural = 'pruebas'
        db_table = 'prueba'


# Create your models here.
class Rast(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.PROTECT)
    distancia = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_uno = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_dos = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_tres = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_quatro = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_cinco = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_seis = models.DecimalField(max_digits=6, decimal_places=2)

    sumatoria_tiempo = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    potencia_uno = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_dos = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_tres = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_quatro = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_cinco = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_seis = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_maxima = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_minima = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_media = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    potencia_relativa = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    indice_fatiga = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    evaluacion = models.CharField(max_length=100, blank=True, null=True)
    normalidad_potencia_maxima = models.CharField(max_length=100, blank=True, null=True)

    def Sumatoria_tiempo_method(self):
        return (self.tiempo_uno + self.tiempo_dos + self.tiempo_tres + self.tiempo_quatro +
                self.tiempo_cinco + self.tiempo_seis)

    def Potencia_uno_method(self):
        return self.prueba.deportista.peso * (self.distancia * self.distancia) / (
                self.tiempo_uno * self.tiempo_uno * self.tiempo_uno)

    def Potencia_dos_method(self):
        return self.prueba.deportista.peso * (self.distancia * self.distancia) / (
                self.tiempo_dos * self.tiempo_dos * self.tiempo_dos)

    def Potencia_tres_method(self):
        return self.prueba.deportista.peso * (self.distancia * self.distancia) / (
                self.tiempo_tres * self.tiempo_tres * self.tiempo_tres)

    def Potencia_quatro_method(self):
        return self.prueba.deportista.peso * (self.distancia * self.distancia) / (
                self.tiempo_quatro * self.tiempo_quatro * self.tiempo_quatro)

    def Potencia_cinco_method(self):
        return self.prueba.deportista.peso * (self.distancia * self.distancia) / (
                self.tiempo_cinco * self.tiempo_cinco * self.tiempo_cinco)

    def Potencia_seis_method(self):
        return self.prueba.deportista.peso * (self.distancia * self.distancia) / (
                self.tiempo_seis * self.tiempo_seis * self.tiempo_seis)

    def Potencia_maxima_method(self):
        potencia_maxima = 0
        if self.Potencia_uno_method() > potencia_maxima:
            potencia_maxima = self.Potencia_uno_method()
        if self.Potencia_dos_method() > potencia_maxima:
            potencia_maxima = self.Potencia_dos_method()
        if self.Potencia_tres_method() > potencia_maxima:
            potencia_maxima = self.Potencia_tres_method()
        if self.Potencia_quatro_method() > potencia_maxima:
            potencia_maxima = self.Potencia_quatro_method()
        if self.Potencia_cinco_method() > potencia_maxima:
            potencia_maxima = self.Potencia_cinco_method()
        if self.Potencia_seis_method() > potencia_maxima:
            potencia_maxima = self.Potencia_seis_method()

        return potencia_maxima

    def Potencia_minima_method(self):
        potencia_minima = self.Potencia_uno_method()
        if self.Potencia_dos_method() < potencia_minima:
            potencia_minima = self.Potencia_dos_method()
        if self.Potencia_tres_method() < potencia_minima:
            potencia_minima = self.Potencia_tres_method()
        if self.Potencia_quatro_method() < potencia_minima:
            potencia_minima = self.Potencia_quatro_method()
        if self.Potencia_cinco_method() < potencia_minima:
            potencia_minima = self.Potencia_cinco_method()
        if self.Potencia_seis_method() < potencia_minima:
            potencia_minima = self.Potencia_seis_method()

        return potencia_minima

    def Potencia_media_method(self):
        return (self.Potencia_uno_method() + self.Potencia_dos_method() + self.Potencia_tres_method() +
                self.Potencia_quatro_method() + self.Potencia_cinco_method() + self.Potencia_seis_method()) / 6

    def Potencia_relativa_method(self):
        return self.Potencia_maxima_method() / self.prueba.deportista.peso

    def Indice_fatiga_method(self):
        return (self.Potencia_maxima_method() - self.Potencia_minima_method()) / self.Sumatoria_tiempo_method()

    def Evaluacion_method(self):
        respuesta = ""
        if self.Indice_fatiga_method() < 10:
            if self.prueba.idioma == 'es':
                respuesta = "Buena capacidad anaerobia"
            elif self.prueba.idioma == 'ru':
                respuesta = "Хорошая анаэробная способность"
            elif self.prueba.idioma == 'in':
                respuesta = "Good anaerobic capacity"
            elif self.prueba.idioma == 'fr':
                respuesta = "Bonne capacité anaérobie"
        else:
            if self.prueba.idioma == 'es':
                respuesta = "Baja capacidad anaerobia"
            elif self.prueba.idioma == 'ru':
                respuesta = "Низкая анаэробная способность"
            elif self.prueba.idioma == 'in':
                respuesta = "Low anaerobic capacity"
            elif self.prueba.idioma == 'fr':
                respuesta = "Faible capacité anaérobie"
        return respuesta

    def Normalidad_potencia_maxima_method(self):
        resultado = ""
        if self.Potencia_maxima_method() < 676:
            if self.prueba.idioma == 'es':
                resultado = "Baja"
            elif self.prueba.idioma == 'ru':
                resultado = "Низкий"
            elif self.prueba.idioma == 'in':
                resultado = "Low"
            elif self.prueba.idioma == 'fr':
                resultado = "Faible"
        if 676 <= self.Potencia_maxima_method() <= 1054:
            if self.prueba.idioma == 'es':
                resultado = "Normal"
            elif self.prueba.idioma == 'ru':
                resultado = "Нормальный"
            elif self.prueba.idioma == 'in':
                resultado = "Normal"
            elif self.prueba.idioma == 'fr':
                resultado = "Normale"
        if self.Potencia_maxima_method() > 1054:
            if self.prueba.idioma == 'es':
                resultado = "Alta"
            elif self.prueba.idioma == 'ru':
                resultado = "высокий"
            elif self.prueba.idioma == 'in':
                resultado = "High"
            elif self.prueba.idioma == 'fr':
                resultado = "Haut"
        return resultado

    def save(self, *args, **kwargs):
        self.potencia_uno = self.Potencia_uno_method()
        self.potencia_dos = self.Potencia_dos_method()
        self.potencia_tres = self.Potencia_tres_method()
        self.potencia_quatro = self.Potencia_quatro_method()
        self.potencia_cinco = self.Potencia_cinco_method()
        self.potencia_seis = self.Potencia_seis_method()
        self.potencia_relativa = self.Potencia_relativa_method()
        self.potencia_maxima = self.Potencia_maxima_method()
        self.sumatoria_tiempo = self.Sumatoria_tiempo_method()
        self.potencia_minima = self.Potencia_minima_method()
        self.potencia_media = self.Potencia_media_method()
        self.indice_fatiga = self.Indice_fatiga_method()
        self.evaluacion = self.Evaluacion_method()
        self.normalidad_potencia_maxima = self.Normalidad_potencia_maxima_method()
        super(Rast, self).save(*args, **kwargs)


class Carlson(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.PROTECT)
    frecuencia_cardiaca_antes = models.IntegerField()
    frecuencia_cardiaca_despues = models.IntegerField()
    frecuencia_cardiaca_min_uno = models.IntegerField()
    frecuencia_cardiaca_min_tres = models.IntegerField()
    frecuencia_cardiaca_min_cinco = models.IntegerField()
    frecuencia_cardiaca_min_siete = models.IntegerField()
    presion_sistolica_antes = models.DecimalField(decimal_places=2, max_digits=6)
    presion_diastolica_antes = models.DecimalField(decimal_places=2, max_digits=6)
    presion_sistolica_despues = models.DecimalField(decimal_places=2, max_digits=6)
    presion_diastolica_despues = models.DecimalField(decimal_places=2, max_digits=6)
    contactos_uno = models.PositiveIntegerField()
    contactos_dos = models.PositiveIntegerField()
    contactos_tres = models.PositiveIntegerField()
    contactos_quatro = models.PositiveIntegerField()
    contactos_cinco = models.PositiveIntegerField()
    contactos_seis = models.PositiveIntegerField()
    contactos_siete = models.PositiveIntegerField()
    contactos_ocho = models.PositiveIntegerField()
    contactos_nueve = models.PositiveIntegerField()
    contactos_diez = models.PositiveIntegerField()

    presion_artereal_diferencial_antes = models.DecimalField(decimal_places=2, max_digits=6)
    presion_artereal_diferencial_despues = models.DecimalField(decimal_places=2, max_digits=6)
    sumatoria_contactos = models.IntegerField()
    reserva_frecuencia = models.IntegerField()
    sumatoria_latidos_recuperacion = models.IntegerField()
    potencia_latidos = models.DecimalField(decimal_places=2, max_digits=12)
    indice_calidad = models.DecimalField(decimal_places=2, max_digits=6)
    evaluacion = models.CharField(null=True, max_length=150, blank=True)

    def Presion_artereal_diferencial_antes(self):
        return self.presion_sistolica_antes - self.presion_diastolica_antes

    def Presion_artereal_diferencial_despues(self):
        return self.presion_sistolica_despues - self.presion_diastolica_despues

    def Sumatoria_contactos(self):
        return (self.contactos_uno + self.contactos_dos + self.contactos_cinco +
                self.contactos_seis + self.contactos_tres + self.contactos_quatro +
                self.contactos_siete + self.contactos_nueve + self.contactos_ocho + self.contactos_diez)

    def Sumatoria_latidos_recuperacion(self):
        return (self.frecuencia_cardiaca_min_uno + self.frecuencia_cardiaca_min_tres +
                self.frecuencia_cardiaca_min_siete + self.frecuencia_cardiaca_min_cinco)

    def Potencia_latidos(self):
        return self.Sumatoria_contactos() / self.Sumatoria_latidos_recuperacion()

    def Indice_calidad(self):
        return (self.Presion_artereal_diferencial_despues() - self.Presion_artereal_diferencial_antes()) / (
                self.frecuencia_cardiaca_despues - self.frecuencia_cardiaca_antes)

    def Reserva_frecuencia(self):
        return self.frecuencia_cardiaca_despues - self.frecuencia_cardiaca_antes

    def Evaluación(self):
        resultado = ""
        if self.Indice_calidad() > 1:
            if self.prueba.idioma == 'es':
                resultado = "Organismo entrenado"
            elif self.prueba.idioma == 'ru':
                resultado = "Тренированный организм"
            elif self.prueba.idioma == 'in':
                resultado = "Trained organism"
            elif self.prueba.idioma == 'fr':
                resultado = "Organisme formé"
        elif 0.5 < self.Indice_calidad() < 1:
            if self.prueba.idioma == 'es':
                resultado = "Normal"
            elif self.prueba.idioma == 'ru':
                resultado = "Нормальный"
            elif self.prueba.idioma == 'in':
                resultado = "Normal"
            elif self.prueba.idioma == 'fr':
                resultado = "Normale"
        else:
            if self.prueba.idioma == 'es':
                resultado = "Poca adaptación al esfuerzo"
            elif self.prueba.idioma == 'ru':
                resultado = "Небольшая адаптация к усилию"
            elif self.prueba.idioma == 'in':
                resultado = "Little adaptation to effort"
            elif self.prueba.idioma == 'fr':
                resultado = "Peu d'adaptation à l'effort"
        return resultado

    def save(self, *args, **kwargs):
        self.presion_artereal_diferencial_antes = self.Presion_artereal_diferencial_antes()
        self.presion_artereal_diferencial_despues = self.Presion_artereal_diferencial_despues()
        self.sumatoria_contactos = self.Sumatoria_contactos()
        self.reserva_frecuencia = self.Reserva_frecuencia()
        self.sumatoria_latidos_recuperacion = self.Sumatoria_latidos_recuperacion()
        self.potencia_latidos = self.Potencia_latidos()
        self.indice_calidad = self.Indice_calidad()
        self.evaluacion = self.Evaluación()
        super(Carlson, self).save(*args, **kwargs)
