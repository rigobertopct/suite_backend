# Generated by Django 3.2.19 on 2024-03-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxeo', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='idioma',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='codifresultado',
            name='idioma',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='configgolpe',
            name='idioma',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='golpe',
            name='idioma',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resultado',
            name='idioma',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]