from django.urls import path, include
from empresas import views as empresas_views
from usuarios import views as usuario_views

urlpatterns = [
    path('', empresas_views.landing, name='landing'),
    
    path('auth/empresa', empresas_views.cadastrar_produtos, name='cadastrar_produtos'),
    path('auth/ver_produtos', empresas_views.ver_produtos, name='ver_produtos'),
    
    path('accounts/cadastrar_empresa', empresas_views.cadastrar_empresa, name='cadastrar_empresa'),
    path('accounts/logar_empresa', empresas_views.logar_empresa, name='logar_empresa'),
    
    path('accounts/cadastrar_usuario', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('accounts/logar_usuario', usuario_views.logar_usuario, name='logar_usuario'),
    
    path('auth/perfil', empresas_views.perfil, name='perfil'),
    path('auth/produtos_comprados', empresas_views.produtos_comprados, name='produtos_comprados'),
    path('auth/ver_produtos/detalhes_produto', empresas_views.detalhes_produto, name='detalhes_produto'),
]