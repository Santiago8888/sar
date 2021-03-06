# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Anyo(models.Model):
  Anyo = models.IntegerField(default=0, null=True, blank=True)

class Mes(models.Model):
  Anyo = models.ForeignKey(Anyo, related_name='mes_anyo', verbose_name='mes_anyo', blank=True, null=True)
  Mes = models.IntegerField(default=0, null=True, blank=True)
  Nombre = models.CharField(max_length=250, default='', blank=True, null=True)

class Semana(models.Model):
  Anyo = models.ForeignKey(Anyo, related_name='semana_anyo', verbose_name='semana_anyo', blank=True, null=True)
  Numero = models.CharField(max_length=250, default='', blank=True, null=True)
  Inicio = models.IntegerField(default=0, blank=True, null=True)
  Fin = models.IntegerField(default=0, blank=True, null=True)
  IMes = models.CharField(max_length=250, default='', blank=True, null=True)
  FMes = models.CharField(max_length=250, default='', blank=True, null=True)

class Dia(models.Model):
  Mes = models.ForeignKey(Mes, related_name='dia_mes', verbose_name='dia_mes', blank=True, null=True)
  Semana = models.ForeignKey(Semana, related_name='semana_dia', verbose_name='semana_dia', blank=True, null=True)
  Dia = models.IntegerField(default=0, null=True, blank=True)

class Negocio(models.Model):
  Nombre = models.CharField(max_length=250, default='', blank=True, null=True)

class Perfil(models.Model):
  Usuario = models.ForeignKey(User, related_name='usuario_perfil', verbose_name='usuario_prefil', blank=True, null=True)
  Negocio = models.ForeignKey(Negocio, related_name='negocio_perfil', verbose_name='negocio_perfil', blank=True, null=True)
  Si = 'Si'
  No = 'No'
  Dicotomia = ((Si, 'Si'),(No, 'No'))
  Administrador = models.CharField(default='No', choices=Dicotomia, max_length=30, null=True, blank=True)
  Owner = models.CharField(default='No', choices=Dicotomia, max_length=30, null=True, blank=True)

class Producto(models.Model):
  Negocio = models.ForeignKey(Negocio, related_name='negocio_producto', verbose_name='negocio_producto', blank=True, null=True)
  Nombre = models.CharField(max_length=250, default='', blank=True, null=True)
  Precio = models.FloatField(default=0, blank=True, null=True)
  Cantidad = models.FloatField(default=0, blank=True, null=True)
  Campo_1 = models.CharField(max_length=250, default='', blank=True, null=True)

class Venta(models.Model):
  Producto = models.ForeignKey(Producto, related_name='producto_venta', verbose_name='producto_venta', blank=True, null=True)
  Perfil = models.ForeignKey(Perfil, related_name='perfil_venta', verbose_name='perfil_venta', blank=True, null=True)
  Dia = models.ForeignKey(Dia, related_name='dia_venta', verbose_name='dia_venta', blank=True, null=True)
  Semana = models.ForeignKey(Semana, related_name='semana_venta', verbose_name='semana_venta', blank=True, null=True)
  Tiempo = models.DateTimeField(auto_now_add=True)
  Cantidad = models.FloatField(default=0, blank=True, null=True)
  Valor_1 = models.CharField(max_length=250, default='', blank=True, null=True)

class Tag(models.Model):
  Dia = models.ForeignKey(Dia, related_name='dia_tag', verbose_name='dia_tag', blank=True, null=True)
  Cantidad = models.FloatField(default=0, blank=True, null=True)
  Total = models.FloatField(default=0, blank=True, null=True)

class Woche(models.Model):
  Semana = models.ForeignKey(Semana, related_name='semana_woche', verbose_name='semana_woche', blank=True, null=True)
  Cantidad = models.FloatField(default=0, blank=True, null=True)
  Total = models.FloatField(default=0, blank=True, null=True)

class Monat(models.Model):
  Mes = models.ForeignKey(Mes, related_name='mes_monat', verbose_name='mes_monat', blank=True, null=True)
  Cantidad = models.FloatField(default=0, blank=True, null=True)
  Total = models.FloatField(default=0, blank=True, null=True)

class Jahre(models.Model):
  Anyo = models.ForeignKey(Anyo, related_name='anyo_jahre', verbose_name='anyo_jahre', blank=True, null=True)
  Cantidad = models.FloatField(default=0, blank=True, null=True)
  Total = models.FloatField(default=0, blank=True, null=True)





  
