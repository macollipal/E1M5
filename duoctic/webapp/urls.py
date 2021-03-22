""":cvar
webapp URL Configuration
"""

from django.urls import path
from . import views


urlpatterns = [
    path('plantilla', views.plantilla, name='plantilla'),
    path('', views.index, name='index'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('docentes', views.docentes, name='docentes'),
    path('contacto', views.contacto, name='contacto'),

]