# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_Directo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedularuc', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=15)),
            ],
        ),
    ]