# Generated by Django 5.0.4 on 2024-05-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControleInscriptions', '0002_ouvrir_fermer_inscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouvrir_fermer_inscription',
            name='IDinscri',
        ),
        migrations.AddField(
            model_name='ouvrir_fermer_inscription',
            name='action',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]