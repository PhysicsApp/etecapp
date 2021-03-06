# -*- coding: utf-8 -*-
from colorful.fields import RGBColorField

from django.db import models
from django.contrib.auth.models import User

from routes.validators import validateConductorUsername


class Conductor(models.Model):
    usuario = models.CharField(validators=[validateConductorUsername, ],
                               max_length=9, unique=True)
    nombre = models.CharField(max_length=80)
    clave = models.CharField(max_length=50, verbose_name='nueva clave',
                             blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'conductores'


class Ruta(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    conductor = models.OneToOneField(Conductor)
    pagina = models.URLField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    color = RGBColorField()

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    auth = models.OneToOneField(User, verbose_name='usuario correspondiente')

    def __str__(self):
        return self.auth.username

    class Meta:
        verbose_name_plural = 'perfiles'


class PerfilRuta(models.Model):
    perfil = models.ForeignKey(Perfil)
    ruta = models.ForeignKey(Ruta)

    def __str__(self):
        return str(self.perfil) + '-' + str(self.ruta)

    class Meta:
        verbose_name = 'suscripción'
        verbose_name_plural = 'suscripciones'
