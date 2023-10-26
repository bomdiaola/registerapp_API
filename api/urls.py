from django.urls import path, include
from rest_framework import routers
from api import views

routers = routers.DefaultRouter()
routers.register(r'alumnos', views.AlumnoViewSet)
routers.register(r'profesores', views.ProfesorViewSet)
routers.register(r'asignaturas', views.AsignaturaViewSet)
routers.register(r'asistencias', views.AsistenciaViewSet)
routers.register(r'codigosqr', views.CodigoQRViewSet)
routers.register(r'matriculas', views.MatriculaViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]