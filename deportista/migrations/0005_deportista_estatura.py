# Generated by Django 3.2.19 on 2024-02-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportista', '0004_auto_20240228_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='deportista',
            name='estatura',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]