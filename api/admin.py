from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Asistencia)
admin.site.register(CodigoQR)
admin.site.register(Matricula)
