# Generated by Django 5.0.2 on 2024-03-16 22:31

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]
