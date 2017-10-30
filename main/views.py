from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
import json

import requests
from lxml.html import fromstring
from datetime import datetime, timedelta, time

import time
import datetime

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
import csv
from io import StringIO

from .models import Contacto_Directo

from django.core import serializers

import geocoder

# Create your views here.

key_contacto_directo = 'pk.eyJ1IjoiYW50aG9ueWgiLCJhIjoiY2o5MGMzY2c5Mnl6bjM0bXJuNnlyMWZmaCJ9.Q0VABADy68PX22RWkPKiMw'


@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    #return render(request,'main/index.html').
    currentuser = request.user
    if currentuser.groups.filter(name='Administradores').exists():
        tipo = "administrador"
    else:
        tipo = "cliente"   
    values={
        'currentuser':currentuser,
        'tipo':tipo
    }
    return render(request, 'main/index.html', values)


@login_required
def contacto_directo(request):

    currentuser = request.user
    if currentuser.groups.filter(name='Administradores').exists():
        tipo = "administrador"
    else:
        tipo = "cliente" 

    if request.POST and request.FILES:

        csvfile = request.FILES['csv_file']
        csvf = StringIO(csvfile.read().decode())
        dataReader = csv.reader(csvf, delimiter=';')
        for row in dataReader:
            if row[0] != 'Cedula Ruc':
                contacto = Contacto_Directo()
                contacto.cedularuc = row[0]
                contacto.nombre = row[1]
                contacto.provincia = row[2]
                contacto.ciudad = row[3]
                contacto.numero = row[4]
                contacto.save()

        contactos = Contacto_Directo.objects.all()

        rows = []
        for contacto in contactos:
            rows.append(contacto.provincia)

        #rows2 = dict.fromkeys(rows).keys()   
        rows2 = list(set(rows)) 
        rows2.sort() 
        #print(rows2)


        values={
            'mensaje':'Su Archivo ha sido añadido',
            'currentuser':currentuser,
            'provincias': rows2,
            'tipo':tipo
        }    
        del csvf, dataReader
        csvfile.close()
        return render(request, 'main/contacto_directo.html', values)

    else:
        contactos = Contacto_Directo.objects.all()
        
        rows = []
        for contacto in contactos:
            rows.append(contacto.provincia)

        #rows2 = dict.fromkeys(rows).keys()
        rows2 = list(set(rows))  
        rows2.sort()  
        #print(rows2)

        values={
            'currentuser':currentuser,
            'provincias': rows2,
            'tipo':tipo
        }    
        return render(request, 'main/contacto_directo.html', values)



"""
def get_contactos(request):
    if request.is_ajax():

        #contactos = Contacto_Directo.objects.all()
        contactos = serializers.serialize("json", Contacto_Directo.objects.all())
        values={
            'contactos': contactos
        }  

        #return HttpResponse(json.dumps(values), content_type='application/json')
        return HttpResponse(json.dumps(contactos), content_type='application/json')
"""


@login_required
def get_contactos1(request, nombre_provincia):
    #currentuser = request.user
    #print(currentuser)
    #Verificamos si el usuario es super
    contactos = Contacto_Directo.objects.filter(provincia=nombre_provincia)

    rows = []
    for contacto in contactos:
        rows.append(contacto.ciudad)
    ciudades = list(set(rows))
    ciudades.sort()

    rows2 = {}
    i = 0
    for ciudad in ciudades:
        rows2[i] = ciudad
        i = i + 1
    #print(rows)
    #ciudades = list(set(rows)) 
    """
    rows = []
    for contacto in contactos:
        rows.append(contacto.provincia)
    ciudades = list(set(rows)) 
    """

    """
    list_carreras = {}
    for carr in carreras:
        list_carreras[carr.codecarre_id] = carr.codecarre.description + " - (" + carr.codecarre.code + ")"
    return HttpResponse(json.dumps(list_carreras))
    """

    #return HttpResponse(json.dumps(rows2))


    f = geocoder.mapbox(nombre_provincia + ', ec', key=key_contacto_directo)
    latlon = f.latlng
    #print(latlon[0])
    latitud = latlon[0]
    longitud = latlon[1]

    values={
        'ciudades':rows2,
        'latitud': latitud,
        'longitud':longitud
    }     

    return HttpResponse(json.dumps(values))


@login_required
def get_contactos2(request, nombre_provincia, nombre_ciudad):
    #currentuser = request.user
    #print(currentuser)
    #Verificamos si el usuario es super
    contactos = Contacto_Directo.objects.filter(provincia=nombre_provincia, ciudad=nombre_ciudad)

    rows = []
    for contacto in contactos:
        rows.append(contacto.nombre)
    nombres = list(set(rows))
    nombres.sort()

    rows2 = {}
    i = 0
    for nombre in nombres:
        rows2[i] = nombre
        i = i + 1


    #return HttpResponse(json.dumps(rows2))



    f = geocoder.mapbox(nombre_ciudad + ', ' + nombre_provincia + ', ec', key=key_contacto_directo)
    #print(f.latlng)
    latlon = f.latlng
    #print(latlon[0])
    latitud = latlon[0]
    longitud = latlon[1]

    values={
        'nombres':rows2,
        'latitud': latitud,
        'longitud':longitud
    }   

    #print(values)

    return HttpResponse(json.dumps(values))



@login_required
def prueba(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    #return render(request,'main/index.html').
    currentuser = request.user
    if currentuser.groups.filter(name='Administradores').exists():
        tipo = "administrador"
    else:
        tipo = "cliente"   
    values={
        'currentuser':currentuser,
        'tipo':tipo
    }
    return render(request, 'main/prueba.html', values)