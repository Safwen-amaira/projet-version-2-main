# Generated by Django 5.0.4 on 2024-05-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chercheur', '0012_alter_chercheur_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chercheur',
            name='image',
            field=models.ImageField(default='image/logo/profile.jpg', upload_to='image/logo/'),
        ),
    ]
