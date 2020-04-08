from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    path('iniciativa/<tipo_iniciativa>/',views.EntidadList.as_view())
    
    

    
    
]