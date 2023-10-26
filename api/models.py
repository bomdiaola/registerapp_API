from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Asistencia(models.Model):
    fecha = models.DateField()
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class CodigoQR(models.Model):
    contenido = models.TextField()
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)