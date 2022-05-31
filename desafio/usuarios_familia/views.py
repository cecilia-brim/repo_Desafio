from django.shortcuts import render
from usuarios_familia.models import familia
from django.http import HttpResponse
import datetime

# Create your views here.

def inicio(request):

    return render(request , "index.html")


def lista_familiares(request):
    Familia = familia.objects.all()
    datos= {"datos" : Familia}

    return render(request , "lista_familiares.html" , datos)

def alta_familiares(request):
    familiar = familia(nombre= "Guillermo" , edad=60 , fecha_nacimiento="1961-02-20" , email= "guillermobrim@gmail.com")
    familiar.save()
    familiar = familia(nombre= "Cecilia" , edad=58 , fecha_nacimiento="1964-02-29", email= "ceciliamaud@gmail.com")
    familiar.save()
    familiar = familia(nombre= "Joaquin" , edad=27 , fecha_nacimiento="1995-05-18" , email= "joaquinbrim@gmail.com")
    familiar.save()
    familiar = familia(nombre= "Sofia" , edad=14 , fecha_nacimiento="2007-07-27" , email= "sofiabrim@gmail.com")


    return HttpResponse("se dio el alta de los familiares")

"""Perfecto María. . Solo te dejo una oportunidad de mejora para las altas, donde podes pasar por parámetros a través de la url, los datos de los familiares... 

Entonces: para el alta de usuarios, sería bueno que no este hardcodeado (Valores fijos en el código).. Una forma facil, es con los queryparams... es decir, cuando llamas a la ruta, por ejemplo ...usuarios/alta_familiar?nombre=juan&edad=30&fecha=1990-03-05 .... fijate que se termina la url... pones un signo de pregunta... y comenzas a dar pares clave=valor... separados por &... y la pregunta es... como los leo en la view... muy facil, lees cada uno con nombre = request.GET.get('nombre', '') , edad= request.GET.get('edad', '') y asi.... Espero te sea de utilidad y lo puedas implementar.. Saludos!!!

"""
