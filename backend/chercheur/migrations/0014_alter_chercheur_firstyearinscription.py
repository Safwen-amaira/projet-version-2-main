# Generated by Django 5.0.4 on 2024-05-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chercheur', '0013_alter_chercheur_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chercheur',
            name='FirstYearInscription',
            field=models.CharField(default='0000', max_length=323, null=True),
        ),
    ]