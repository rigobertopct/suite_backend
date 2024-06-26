# Generated by Django 3.2.19 on 2024-03-06 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deportes', '0003_alter_disciplina_deporte'),
        ('deportista', '0006_alter_deportista_disciplina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deportista',
            name='disciplina',
        ),
        migrations.CreateModel(
            name='DeportistaDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deportista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='deportista.deportista')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Deportes.disciplina')),
            ],
        ),
    ]
