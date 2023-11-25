from django.contrib import admin
from docentes.models import Docente, Materia, Institucion, Alumno

# Register your models here.

admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Institucion)
admin.site.register(Alumno)
