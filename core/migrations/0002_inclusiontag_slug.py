# Generated by Django 4.2.3 on 2023-07-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inclusiontag',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
