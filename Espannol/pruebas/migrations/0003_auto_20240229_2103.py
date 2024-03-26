# Generated by Django 3.2.19 on 2024-03-01 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0002_prueba_etapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rast',
            name='indice_fatiga',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_cinco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_dos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_maxima',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_media',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_minima',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_quatro',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_relativa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_seis',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_tres',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='rast',
            name='potencia_uno',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
    ]
