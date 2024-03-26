# Generated by Django 3.2.19 on 2024-02-28 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deportista', '0004_auto_20240228_1426'),
        ('seguridad', '0002_auto_20240228_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seguridad.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('archivo', models.FileField(blank=True, null=True, upload_to='')),
                ('observaciones', models.CharField(blank=True, max_length=255, null=True)),
                ('valoracion', models.CharField(blank=True, max_length=255, null=True)),
                ('deportista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='deportista.deportista')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruebas.lugar')),
            ],
            options={
                'verbose_name': 'prueba',
                'verbose_name_plural': 'pruebas',
                'db_table': 'prueba',
            },
        ),
        migrations.CreateModel(
            name='Rast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiempo_uno', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiempo_dos', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiempo_tres', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiempo_quatro', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiempo_cinco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tiempo_seis', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sumatoria_tiempo', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_uno', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_dos', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_tres', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_quatro', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_cinco', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_seis', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_maxima', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_minima', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_media', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('potencia_relativa', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('indice_fatiga', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('evaluacion', models.CharField(blank=True, max_length=100, null=True)),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruebas.prueba')),
            ],
        ),
        migrations.CreateModel(
            name='Carlson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_cardiaca_antes', models.IntegerField()),
                ('frecuencia_cardiaca_despues', models.IntegerField()),
                ('frecuencia_cardiaca_min_uno', models.IntegerField()),
                ('frecuencia_cardiaca_min_tres', models.IntegerField()),
                ('frecuencia_cardiaca_min_cinco', models.IntegerField()),
                ('frecuencia_cardiaca_min_siete', models.IntegerField()),
                ('presion_sistolica_antes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('presion_diastolica_antes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('presion_sistolica_despues', models.DecimalField(decimal_places=2, max_digits=6)),
                ('presion_diastolica_despues', models.DecimalField(decimal_places=2, max_digits=6)),
                ('contactos_uno', models.PositiveIntegerField()),
                ('contactos_dos', models.PositiveIntegerField()),
                ('contactos_tres', models.PositiveIntegerField()),
                ('contactos_quatro', models.PositiveIntegerField()),
                ('contactos_cinco', models.PositiveIntegerField()),
                ('contactos_seis', models.PositiveIntegerField()),
                ('contactos_siete', models.PositiveIntegerField()),
                ('contactos_ocho', models.PositiveIntegerField()),
                ('contactos_nueve', models.PositiveIntegerField()),
                ('contactos_diez', models.PositiveIntegerField()),
                ('presion_artereal_diferencial_antes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('presion_artereal_diferencial_despues', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sumatoria_contactos', models.IntegerField()),
                ('reserva_frecuencia', models.IntegerField()),
                ('sumatoria_latidos_recuperacion', models.IntegerField()),
                ('potencia_latidos', models.DecimalField(decimal_places=2, max_digits=12)),
                ('indice_calidad', models.DecimalField(decimal_places=2, max_digits=6)),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruebas.prueba')),
            ],
        ),
    ]