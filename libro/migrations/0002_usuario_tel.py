# Generated by Django 4.0.6 on 2022-08-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tel',
            field=models.CharField(default='tel', max_length=10),
            preserve_default=False,
        ),
    ]
