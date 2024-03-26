# Generated by Django 3.2.19 on 2024-02-26 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='Nombre y Apellidos')),
                ('edad', models.PositiveIntegerField(null=True)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pugiles')),
                ('ci', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('anno_deporte', models.IntegerField(blank=True, null=True)),
                ('anno_nacional', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomencladores.pais')),
            ],
        ),
    ]