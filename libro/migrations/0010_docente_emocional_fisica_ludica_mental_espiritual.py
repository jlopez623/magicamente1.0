# Generated by Django 4.0.6 on 2023-01-15 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libro', '0009_delete_profiles_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=20, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=20, verbose_name='Apellido Materno')),
                ('nombres', models.CharField(max_length=20, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='F', max_length=1)),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'db_table': 'docente',
                'ordering': ['apellido_paterno', '-apellido_materno'],
            },
        ),
        migrations.CreateModel(
            name='Emocional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emocional_23', models.IntegerField(verbose_name='23')),
                ('emocional_41', models.IntegerField(verbose_name='41')),
                ('emocional_43', models.IntegerField(verbose_name='43')),
                ('emocional_50', models.IntegerField(verbose_name='50')),
                ('emocional_59', models.IntegerField(verbose_name='59')),
                ('emocional_61', models.IntegerField(verbose_name='61')),
                ('emocional_65', models.IntegerField(verbose_name='65')),
                ('emocional_67', models.IntegerField(verbose_name='67')),
                ('emocional_total', models.IntegerField(verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='Fisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisica_3', models.IntegerField(verbose_name='3')),
                ('fisica_6', models.IntegerField(verbose_name='6')),
                ('fisica_9', models.IntegerField(verbose_name='9')),
                ('fisica_14', models.IntegerField(verbose_name='14')),
                ('fisica_16', models.IntegerField(verbose_name='16')),
                ('fisica_29', models.IntegerField(verbose_name='29')),
                ('fisica_32', models.IntegerField(verbose_name='32')),
                ('fisica_48', models.IntegerField(verbose_name='48')),
                ('fisica_total', models.IntegerField(verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='Ludica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mental_1', models.IntegerField(verbose_name='2')),
                ('mental_11', models.IntegerField(verbose_name='5')),
                ('mental_47', models.IntegerField(verbose_name='19')),
                ('mental_52', models.IntegerField(verbose_name='21')),
                ('mental_55', models.IntegerField(verbose_name='25')),
                ('mental_58', models.IntegerField(verbose_name='35')),
                ('mental_62', models.IntegerField(verbose_name='37')),
                ('mental_68', models.IntegerField(verbose_name='40')),
                ('mental_total', models.IntegerField(verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='Mental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mental_2', models.IntegerField(verbose_name='2')),
                ('mental_5', models.IntegerField(verbose_name='5')),
                ('mental_19', models.IntegerField(verbose_name='19')),
                ('mental_21', models.IntegerField(verbose_name='21')),
                ('mental_25', models.IntegerField(verbose_name='25')),
                ('mental_35', models.IntegerField(verbose_name='35')),
                ('mental_37', models.IntegerField(verbose_name='37')),
                ('mental_40', models.IntegerField(verbose_name='40')),
                ('mental_total', models.IntegerField(verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='Espiritual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espiritual_4', models.IntegerField(verbose_name='4')),
                ('espiritual_17', models.IntegerField(verbose_name='17')),
                ('espiritual_30', models.IntegerField(verbose_name='30')),
                ('espiritual_33', models.IntegerField(verbose_name='33')),
                ('espiritual_39', models.IntegerField(verbose_name='39')),
                ('espiritual_49', models.IntegerField(verbose_name='49')),
                ('espiritual_56', models.IntegerField(verbose_name='56')),
                ('espiritual_60', models.IntegerField(verbose_name='60')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]