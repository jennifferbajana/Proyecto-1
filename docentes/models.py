from django.db import models


# Create your models here.
class Institucion(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.nombre}'


class Alumno(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=20, null=True)
    apellido = models.CharField(max_length=20)
    cedula = models.CharField(max_length=10)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)
    fecha_de_nacimiento = models.CharField(max_length=50)
    celular = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id} - {self.apellido} {self.nombre}'


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    horas = models.IntegerField(null=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}'


class Docente(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.CharField(max_length=10)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)
    materia = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True)
    fecha_de_nacimiento = models.CharField(max_length=50)
    celular = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.apellido} {self.nombre}'
