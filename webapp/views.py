from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from docentes.models import Docente


# Create your views here.
def bienvenida(request):
    return HttpResponse ('Saludos')


def bienvenida2(request):
    cantidad_docentes = Docente.objects.count()
    #docentes = Docente.objects.all()
    docentes = Docente.objects.order_by('apellido','nombre')
    #print(f'Cantidad  docentes:{cantidad_docentes}')
    dict_datos = {'cantidad_docentes': cantidad_docentes, 'docentes': docentes}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos, request))
