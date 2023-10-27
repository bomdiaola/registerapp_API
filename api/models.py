from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#establece el tipo de usuario
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Profesor(models.Model):#Profesor tiene el nombre, el email y la contraseña y su tipo de usuario, Profesor, ADMIM o Alumno
    user = models.OneToOneField(User, on_delete=models.CASCADE)#establece el tipo de usuario
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Asignatura(models.Model): #Asignatura tiene el titulo, el horario de cuando se imparte la clase y el profesor que la imparte
    titulo = models.CharField(max_length=100, default="Sin titulo")
    horario = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Asistencia(models.Model):#Asistencia tiene la fecha y hora de la asistencia, la asignatura a la que pertenece y el alumno que asiste
    fecha_hora = models.DateTimeField(default=timezone.now)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class CodigoQR(models.Model):#CodigoQR tiene la fecha de generacion del codigo, la asistencia a la que pertenece y el codigo en si
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

class Matricula(models.Model):#Matricula tiene el alumno y la asignatura a la que pertenece
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    #si un estudiante se matricula en varias asignaturas a lo largo del tiempo, 
    # puedes crear una instancia de Matricula para cada una de esas matrículas, 
    # relacionando al alumno y la asignatura correspondiente. En conclusion
    #Esta clase sirve para que el alumno pueda registrarse en varias asignaturas a la vez.