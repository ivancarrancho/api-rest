# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Nombre del libro'
    )

    age = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha'
    )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

class Author(models.Model):
    DOCUMENT_TYPE_CHOICES = (
    ('10', 'Cédula'),
    ('20', 'Tarjeta de identidad'),
    ('30', 'Pasaporte'),
    ('40', 'Lo robaron'),
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Nombre del autor'
    )

    document_type = models.CharField(
        choices=DOCUMENT_TYPE_CHOICES,
        verbose_name='tipo de documento',
        max_length=20,
    )

    class Meta:
        verbose_name = 'autor',
        verbose_name_plural = 'autores'

