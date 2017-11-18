from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pro/(?P<key>[0-9]+)/$', views.proAdd, name='proAdd'),
    url(r'^maalik/(?:(?P<dia>[0-9]+)/)?(?:(?P<mes>[0-9]+)/)?(?:(?P<anyo>[0-9]+)/)?$', views.maalik, name='maalik'),
    url(r'^maalik/imera/(?P<dia>[0-9]+)/$', views.maalikDia, name='maalikDia'),
    url(r'^maalik/saptaah/(?P<sem>[0-9]+)/$', views.maalikSem, name='maalikSem'),
    url(r'^maalik/maheena/(?P<mes>[0-9]+)/$', views.maalikMes, name='maalikMes'),
    url(r'^maalik/saal/(?P<anyo>[0-9]+)/$', views.maalikAnyo, name='maalikAnyo'),
    url(r'^maalik/imera/(?P<dia>[0-9]+)/bayani/$', views.maalikDiaBay, name='maalikDiaBay'),
    url(r'^maalik/saptaah/(?P<sem>[0-9]+)/bayani/$', views.maalikSemBay, name='maalikSemBay'),
    url(r'^maalik/maheena/(?P<mes>[0-9]+)/bayani/$', views.maalikMesBay, name='maalikMesBay'),
    url(r'^maalik/saal/(?P<anyo>[0-9]+)/bayani/$', views.maalikAnyoBay, name='maalikAnyoBay'),
]





