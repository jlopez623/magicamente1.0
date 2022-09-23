# Generated by Django 4.1.1 on 2022-09-22 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libro', '0003_remove_usuario_tel_alter_codebook_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='birth',
            field=models.DateField(null=True, verbose_name='fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='movil',
            field=models.CharField(max_length=10, null=True, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='contraseña'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(max_length=20, verbose_name='Apellido'),
        ),
        migrations.CreateModel(
            name='UsuarioInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descripción', models.TimeField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateField(null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
