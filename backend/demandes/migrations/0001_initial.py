# Generated by Django 5.0.2 on 2024-04-14 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeDemande', models.CharField(max_length=200)),
                ('nomChercheur', models.CharField(max_length=100)),
                ('prenomChercheur', models.CharField(max_length=200)),
                ('cin', models.CharField(max_length=200)),
                ('tel', models.CharField(default='none', max_length=30)),
                ('SujetThese', models.TextField(default='none')),
                ('Address', models.TextField(default='none')),
                ('dateNaissance', models.DateField(default='0000-00-00')),
                ('lieuNaissance', models.CharField(max_length=255)),
                ('StructureRecherche', models.CharField(max_length=255)),
                ('specialite', models.CharField(max_length=255)),
                ('niveau', models.CharField(max_length=200)),
                ('TypeThese', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('DateDepot', models.DateField(default=datetime.date.today)),
                ('State', models.CharField(default='En attente', max_length=244)),
            ],
        ),
    ]
