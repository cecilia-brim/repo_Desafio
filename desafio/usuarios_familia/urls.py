from django.urls import URLPattern, path 
from.import views


urlpatterns = [

    path("" , views.inicio) ,
    path("lista_familiares" , views.lista_familiares) ,   
    path("alta_familiares" , views.alta_familiares)


]