# Generated by Django 4.0.6 on 2023-01-11 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0008_codebook_user_profiles_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profiles_photo',
        ),
    ]
