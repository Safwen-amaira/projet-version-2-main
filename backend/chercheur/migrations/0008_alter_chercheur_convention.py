# Generated by Django 5.0.4 on 2024-04-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chercheur', '0007_alter_chercheur_datenaissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chercheur',
            name='convention',
            field=models.FileField(default=1, upload_to='store/files/'),
            preserve_default=False,
        ),
    ]