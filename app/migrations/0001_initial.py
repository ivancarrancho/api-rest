# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre del autor')),
                ('document_type', models.CharField(choices=[('10', 'C\xe9dula'), ('20', 'Tarjeta de identidad'), ('30', 'Pasaporte'), ('40', 'Lo robaron')], max_length=20, verbose_name='tipo de documento')),
            ],
            options={
                'verbose_name': ('autor',),
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del libro')),
                ('age', models.DateField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
