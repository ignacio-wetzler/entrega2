# Generated by Django 4.1.3 on 2023-01-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_rename_perfil_profile_rename_imagen_profile_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='usuario',
        ),
    ]
