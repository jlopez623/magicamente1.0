# Generated by Django 4.1.1 on 2022-09-22 20:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libro', '0004_usuario_birth_usuario_movil_usuario_password_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsuarioInfo',
            new_name='Task',
        ),
    ]
