# Generated by Django 5.0.4 on 2024-05-24 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centrerecherche', '0001_initial'),
        ('etablissement', '0002_gereretablissement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labo',
            name='Etablissement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.etablissement'),
        ),
    ]
