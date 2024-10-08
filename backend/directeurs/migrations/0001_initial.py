# Generated by Django 5.0.4 on 2024-05-09 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centrerecherche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=400)),
                ('grade', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('numTel', models.CharField(max_length=200)),
                ('specialite', models.CharField(max_length=200)),
                ('lieuTravail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='centrerecherche.labo')),
            ],
        ),
    ]
