# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=80)),
                ('segundo_nombre', models.CharField(blank=True, max_length=80)),
                ('primer_apellido', models.CharField(max_length=80)),
                ('segundo_apellido', models.CharField(max_length=80)),
                ('identidicacion', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=150)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('codigo', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=80)),
                ('segundo_nombre', models.CharField(blank=True, max_length=80)),
                ('primer_apellido', models.CharField(max_length=80)),
                ('segundo_apellido', models.CharField(max_length=80)),
                ('identidicacion', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=150)),
                ('correo', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
