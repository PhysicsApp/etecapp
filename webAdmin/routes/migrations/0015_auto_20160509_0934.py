# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import routes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0014_conductor_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='usuario',
            field=models.CharField(max_length=9, unique=True, validators=[routes.validators.validateConductorUsername]),
        ),
    ]