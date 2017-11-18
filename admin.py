# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Negocio, Perfil, Producto, Venta, Anyo, Mes, Semana, Dia, Tag, Woche, Monat, Jahre

admin.site.register(Anyo)
admin.site.register(Mes)
admin.site.register(Semana)
admin.site.register(Dia)
admin.site.register(Negocio)
admin.site.register(Perfil)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Tag)
admin.site.register(Monat)
admin.site.register(Woche)
admin.site.register(Jahre)

