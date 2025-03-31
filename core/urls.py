from django.urls import path, include
from empresas import views as empresas_views

urlpatterns = [
    path('empresas/', include('empresas.urls')),
    path('auth/empresa', empresas_views.index, name='home'),
    path('', empresas_views.landing, name='landing'),
]
