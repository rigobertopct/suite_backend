# Generated by Django 3.2.19 on 2024-02-26 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boxeo', '0001_initial'),
        ('nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configgolpe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='combate',
            name='esquinaA',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='person', to='boxeo.pugil'),
        ),
        migrations.AddField(
            model_name='combate',
            name='esquinaR',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='person1', to='boxeo.pugil'),
        ),
        migrations.AddField(
            model_name='combate',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nomencladores.evento'),
        ),
    ]