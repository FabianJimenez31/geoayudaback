from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Return available departments - GET
    path('departamentos/',views.DepartamentosList.as_view()),
    # Return available cities - GET
    path('ciudades/',views.CiudadesList.as_view()),
    # Return all cities available on department
    path('ciudades/<departamento_id>',views.CiudadesByDepartment.as_view()),
    # Return Initiatives by department - POST - Department
    path('iniciativas/<ciudad_id>/',views.IniciativasByCiudad.as_view()),
    # Return Initiatives by type
    path('iniciativa/<tipo_iniciativa>/',views.EntidadList.as_view())  
]