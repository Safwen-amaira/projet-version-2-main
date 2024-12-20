# Generated by Django 5.0.4 on 2024-05-23 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chercheur', '0011_chercheur_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=400)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(default='non-vu', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chercheur.chercheur')),
            ],
        ),
    ]
