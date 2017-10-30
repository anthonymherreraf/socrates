from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contactodirecto/', views.contacto_directo, name='contacto_directo'),
    url(r'^prueba/', views.prueba, name='prueba'),
    #url(r'^get/contactos/$', views.get_contactos, name='get_contactos'),
    url(r'^get/contactos1/(?P<nombre_provincia>[0-9a-zA-Z% ]+)/$', views.get_contactos1, name='get_contactos1'),
    url(r'^get/contactos2/(?P<nombre_provincia>[0-9a-zA-Z% ]+)/(?P<nombre_ciudad>[0-9a-zA-Z% ]+)/$', views.get_contactos2, name='get_contactos2'),
]