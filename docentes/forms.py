from django.forms import ModelForm, EmailInput

from docentes.models import Docente


class DocenteFormulario(ModelForm):
    class Meta:
        model = Docente
        fields = ('nombre', 'apellido', 'sexo', 'email', 'activo', 'materia', 'institucion', 'cedula', 'celular', 'fecha_de_nacimiento')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }