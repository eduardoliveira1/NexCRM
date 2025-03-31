from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('logar_empresa/', views.logar_empresa, name='logar_empresa'),
    path('perfil/', views.perfil, name='perfil'),
]
