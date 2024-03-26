# Generated by Django 3.2.19 on 2024-02-28 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deportes', '0002_disciplina_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='deporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Deportes.deporte'),
        ),
    ]