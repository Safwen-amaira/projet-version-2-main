# Generated by Django 5.0.2 on 2024-04-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preinscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Opertator_Name', models.CharField(max_length=100)),
                ('is_open', models.BooleanField(default=True)),
                ('end_date', models.DateField()),
            ],
        ),
    ]