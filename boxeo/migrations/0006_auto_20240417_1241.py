# Generated by Django 3.2.19 on 2024-04-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxeo', '0005_auto_20240417_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='peso_max',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='peso_min',
            field=models.CharField(max_length=100),
        ),
    ]
