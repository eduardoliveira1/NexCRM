from .models import Empresa
from usuarios.models import Usuario, Produto

def get_empresa_logada(request):
    empresa_logada_id = request.session.get('empresa_logada_id')
    if empresa_logada_id:
        try:
            return Empresa.objects.get(id=empresa_logada_id)
        except Empresa.DoesNotExist:
            return None
    return None

def efetuar_login_empresa(dono_empresa, nome_empresa):
    empresa = Empresa.objects.get(nome_empresa=nome_empresa)
    if empresa:
        if dono_empresa == empresa.dono_empresa:
            return empresa 
    return None 

def get_usuario_logado(request):
    usuario_logado_id = request.session.get('usuario_logado_id')
    if usuario_logado_id:
        try:
            return Usuario.objects.get(id=usuario_logado_id)
        except Usuario.DoesNotExist:
            return None
    return None
      
def efetuar_login_usuario(email, senha):
    usuario = Usuario.objects.get(email=email)
    if usuario:
        if senha == usuario.senha:
            return usuario 
    return None

def get_produto_escolhido(request):
    produto_escolhido_id = request.session.get('produto_escolhido_id')
    if produto_escolhido_id:
        try:
            return Produto.objects.get(id=produto_escolhido_id)
        except Produto.DoesNotExist:
            return None
    return None