# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Negocio, Perfil, Producto, Venta, Dia, Mes, Anyo, Semana, Tag, Woche, Monat, Jahre
from django.http import HttpResponseRedirect
from datetime import datetime, date, time
from django.http import HttpResponse
from django.shortcuts import render
from pytz import all_timezones

def finD(dia):
  Ven = Venta.objects.filter(Dia=dia)
  JJP = Tag.objects.get_or_create(Dia=dia)[0]
  Res = [0,0]
  for ven in Ven:
    Res[0] = Res[0] + ven.Cantidad
    Res[1] = Res[1] + ven.Cantidad*ven.Producto.Precio
  JJP.Cantidad = Res[0]
  JJP.Total = Res[1]
  JJP.save()
  return None  

def finS(semana):
  Ven = Tag.objects.filter(Dia__Semana=semana)
  JJP = Woche.objects.get_or_create(Semana=semana)[0]
  Res = [0,0]
  for ven in Ven:
    Res[0] = Res[0] + ven.Cantidad
    Res[1] = Res[1] + ven.Total
  JJP.Cantidad = Res[0]
  JJP.Total = Res[1]
  JJP.save()
  return None  

def finM(mes):
  Ven = Tag.objects.filter(Dia__Mes=mes)
  JJP = Monat.objects.get_or_create(Mes=mes)[0]
  Res = [0,0]
  for ven in Ven:
    Res[0] = Res[0] + ven.Cantidad
    Res[1] = Res[1] + ven.Total
  JJP.Cantidad = Res[0]
  JJP.Total = Res[1]
  JJP.save()
  return None  

def tiempo():
  date2 = date.today()
  if str(date2.year) == str(Anyo.objects.last().Anyo):
    A = Anyo.objects.get(Anyo=date2.year)
  else:
    Anyo.objects.create(Anyo=date2.year)
    A = Anyo.objects.get(Anyo=date2.year)
  if str(date2.month) == str(Mes.objects.last().Mes):
    M = Mes.objects.get(Mes=date2.month, Anyo = A)
  else:
    Mes.objects.create(Mes=date2.month, Anyo = A)
    M = Mes.objects.get(Mes=date2.month, Anyo = A)
  if str(date2.isocalendar()[1]) == str(Semana.objects.last().Numero):
    S = Semana.objects.last()
  else:
    finS(Semana.objects.last())
    Semana.objects.create(Numero=date2.isocalendar()[1])
    S = Semana.objects.last()
  if str(date2.day) == str(Dia.objects.last().Dia):
    D = Dia.objects.get(Dia = date2.day, Mes = M)
  else:
    finD(Dia.objects.last())
    Dia.objects.create(Dia=date2.day, Mes = M, Semana = S)
    D = Dia.objects.get(Dia = date2.day, Mes = M)
  return [A,M,D,S]

def temps(alldata):
    dD = alldata.get("dateD", "0")
    dS = alldata.get("dateS", "0")
    dM = alldata.get("date", "0")
    dY = alldata.get("dateY", "0")
    if len(dD) > 0:
      kay = dD[:2]
      koy = dD[3:5]
      kuy = dD[6:]
      try:
        a = Anyo.objects.get(Anyo=kuy)
        m = Mes.objects.get(Mes=koy, Anyo=a)
        d = Dia.objects.get(Dia=kay, Mes=m)
        return '/sar/maalik/imera/'+str(d.pk)+'/'
      except:
        d = Dia.objects.last()
        return '/sar/maalik/imera/'+str(d.pk)+'/'
    if len(dS) > 0:
      kay = dS[:2]
      koy = dS[3:5]
      kuy = dS[6:10]
      date2 = datetime.strptime(kay+koy+kuy, "%d%m%Y").date()
      s = date2.isocalendar()[1]
      try:
        s = Semana.objects.get(Numero=s)
      except:
        s = Semana.objects.last()
      return '/sar/maalik/saptaah/'+str(s.pk)+'/'
    if len(dM) > 0:
      koy = dM[:2]
      kuy = dM[3:]
      try:
        a = Anyo.objects.get(Anyo=kuy)
        m = Mes.objects.get(Mes=koy, Anyo=a)
      except:
        m = Mes.objects.last()
      return '/sar/maalik/maheena/'+str(m.pk)+'/'
    if len(dY) > 0:
      kuy = dY
      try:
        y = Anyo.objects.get(Anyo=kuy)
      except:
        y = Anyo.objects.last()
      return '/sar/maalik/saal/'+str(y.pk)+'/'

def sell(request):
  return None

def index(request):
  tiempo()
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio  
  pro = Producto.objects.filter(Negocio=neg)
  if request.method == 'POST':
    alldata = request.POST
    dD = alldata.get("dateD", "0")
    dS = alldata.get("dateS", "0")
    dM = alldata.get("date", "0")
    dY = alldata.get("dateY", "0")
    if len(dD) > 0:
      kay = dD[:2]
      koy = dD[3:5]
      kuy = dD[6:]
      try:
        a = Anyo.objects.get(Anyo=kuy)
        m = Mes.objects.get(Mes=koy, Anyo=a)
        d = Dia.objects.get(Dia=kay, Mes=m)
        return HttpResponseRedirect('maalik/imera/'+str(d.pk)+'/')
      except:
        pass
      return HttpResponse('success')
    if len(dS) > 0:
      return None
    if len(dM) > 0:
      return None
    if len(dY) > 0:
      return None
  if perfil.Owner == 'Si':
    V = Venta.objects.filter(Producto__Negocio=neg)
    total = [0,0]    
    for v in V:
      total[0] = total[0] + v.Cantidad
      total[1] = total[1] + (v.Cantidad*v.Producto.Precio)
    context = {'neg':neg, 'pro':pro, 'V':V, 'total':total}
    return render(request, 'sar/index.html', context)
  else:
    context = {'neg':neg, 'pro':pro}
    return render(request, 'sar/indexC.html', context)
 
def proAdd(request, key):
  T = tiempo()
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio  
  pro = Producto.objects.get(pk=key)
  if request.method == 'POST':
    alldata = request.POST
    dat = [alldata.get("Cantidad","0"),alldata.get(pro.Campo_1, "0")]
    Venta.objects.create(Producto=pro, Perfil=perfil, Cantidad=dat[0], Valor_1=dat[1], Dia = T[2], Semana = T[3])
    return HttpResponseRedirect('/sar/')
  context = {'neg':neg, 'pro':pro}
  return render(request, 'sar/proAdd.html', context)

def maalik(request, dia=None, mes=None, anyo=None):
  Hola = str(dia)+' '+str(mes)+' '+str(anyo)
  return HttpResponse(Hola)

def maalikDia(request, dia):
  finD(Dia.objects.last())
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(temps(alldata))
  d = Dia.objects.get(pk=dia)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio  
  pro = Producto.objects.filter(Negocio=neg)
  P = []
  for p in pro:
    V = Venta.objects.filter(Producto=p, Dia=d)
    total = [0,0,p.Nombre]
    for v in V:
      total[0] = total[0] + v.Cantidad
      total[1] = total[1] + (v.Cantidad*v.Producto.Precio)
    if V.count() > 0:
      P.append(total)
  total = [0,0]
  for p in P:
    total[0] = total[0] + p[0] 
    total[1] = total[1] + p[1] 
  context = {'neg':neg, 'pro':pro, 'P':P, 'total':total}
  return render(request, 'sar/maalik.html', context)

def maalikSem(request, sem):
  finS(Semana.objects.last())
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(temps(alldata))
  s = Semana.objects.get(pk=sem)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio
  D = Tag.objects.filter(Dia__Semana=s)  
  total = [0,0]
  for d in D:
    total[0] = total[0] + d.Cantidad
    total[1] = total[1] + (d.Total)
  context = {'neg':neg, 'D':D, 'total':total}
  return render(request, 'sar/maalikSaptaah.html', context)

def maalikMes(request, mes):
  finM(Mes.objects.last())
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(temps(alldata))
  m = Mes.objects.get(pk=mes)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio
  date2 = datetime.strptime('01'+str(m.Mes)+str(m.Anyo.Anyo), "%d%m%Y").date()
  es = date2.isocalendar()[1]
  S = []
  for i in range(1,6):
    try:
      S.append(Woche.objects.get(Semana__Numero=es+i))
    except:
      pass
  total = [0,0]
  for s in S:
    total[0] = total[0] + s.Cantidad
    total[1] = total[1] + (s.Total)
  context = {'neg':neg, 'S':S, 'total':total}
  return render(request, 'sar/maalikMaheena.html', context)

def maalikAnyo(request, anyo):
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(temps(alldata))
  a = Anyo.objects.get(pk=anyo)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio
  M = Monat.objects.filter(Mes__Anyo=a)
  total = [0,0]
  for m in M:
    total[0] = total[0] + m.Cantidad
    total[1] = total[1] + m.Total
  context = {'neg':neg, 'M':M, 'total':total}
  return render(request, 'sar/maalikSaal.html', context)

def maalikDiaBay(request, dia):
  finD(Dia.objects.last())
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(str(temps(alldata))+'bayani/')
  d = Dia.objects.get(pk=dia)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio  
  pro = Producto.objects.filter(Negocio=neg)
  P = []
  for p in pro:
    V = Venta.objects.filter(Producto=p, Dia=d)
    total = [0,0,p.Nombre]
    for v in V:
      total[0] = total[0] + v.Cantidad
      total[1] = total[1] + (v.Cantidad*v.Producto.Precio)
    if V.count() > 0:
      P.append(total)
  total = [0,0]
  for p in P:
    total[0] = total[0] + p[0] 
    total[1] = total[1] + p[1] 
  context = {'neg':neg, 'pro':pro, 'P':P, 'total':total}
  return render(request, 'sar/maalikBay.html', context)

def maalikSemBay(request, sem):
  finS(Semana.objects.last())
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(str(temps(alldata))+'bayani/')
  s = Semana.objects.get(pk=sem)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio
  P = Tag.objects.filter(Dia__Semana=s)  
  total = [0,0]
  for d in P:
    total[0] = total[0] + d.Cantidad
    total[1] = total[1] + (d.Total)
  context = {'neg':neg, 'P':P, 'total':total}
  return render(request, 'sar/maalikSaptaahBay.html', context)

def maalikMesBay(request, mes):
  finM(Mes.objects.last())
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(str(temps(alldata))+'bayani/')
  m = Mes.objects.get(pk=mes)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio
  date2 = datetime.strptime('01'+str(m.Mes)+str(m.Anyo.Anyo), "%d%m%Y").date()
  es = date2.isocalendar()[1]
  S = []
  for i in range(1,6):
    try:
      S.append(Woche.objects.get(Semana__Numero=es+i))
    except:
      pass
  total = [0,0]
  for s in S:
    total[0] = total[0] + s.Cantidad
    total[1] = total[1] + (s.Total)
  context = {'neg':neg, 'P':S, 'total':total}
  return render(request, 'sar/maalikMaheenaBay.html', context)

def maalikAnyoBay(request, anyo):
  if request.method == 'POST':
    alldata = request.POST
    return HttpResponseRedirect(str(temps(alldata))+'bayani/')
  a = Anyo.objects.get(pk=anyo)
  current_user = request.user
  perfil = Perfil.objects.get(Usuario=current_user)
  neg = perfil.Negocio
  M = Monat.objects.filter(Mes__Anyo=a)
  total = [0,0]
  for m in M:
    total[0] = total[0] + m.Cantidad
    total[1] = total[1] + m.Total
  context = {'neg':neg, 'P':M, 'total':total}
  return render(request, 'sar/maalikSaalBay.html', context)


