# Generated by Django 5.0.4 on 2024-05-16 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chercheur', '0008_alter_chercheur_convention'),
        ('demandes', '0003_alter_demandes_datedepot_alter_demandes_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandes',
            name='cin',
        ),
        migrations.AddField(
            model_name='demandes',
            name='chercheur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chercheur.chercheur'),
        ),
    ]
