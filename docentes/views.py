from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from docentes.forms import DocenteFormulario
from docentes.models import Docente

# Create your views here.
DocenteFormulario = modelform_factory(Docente, exclude=['activo',])
# Create your views here.
def agregar_docente(request):
    pagina = loader.get_template('docentes/agregar.html')
    if request.method == 'GET':
        formulario = DocenteFormulario
    elif request.method == 'POST':
        formulario = DocenteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def modificar_docente(request, id):
    pagina = loader.get_template('docentes/modificar.html')
    docente = get_object_or_404(Docente, pk=id)
    if request.method == 'GET':
        formulario = DocenteFormulario(instance=docente)
    elif request.method == 'POST':
        formulario = DocenteFormulario(request.POST, instance=docente )
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_docente(request, id):
    #docente = Docente.objects.get(pk=id)
    docente = get_object_or_404(Docente, pk=id)
    datos ={'docente': docente}
    print(docente)
    pagina = loader.get_template('docentes/ver.html')
    return HttpResponse(pagina.render(datos, request))

def eliminar_docente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    if docente:
        docente.delete()
        return redirect('inicio')

# Create your views here.