# Generated by Django 5.0.4 on 2024-04-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=400)),
                ('date_creation', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
