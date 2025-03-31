from django.shortcuts import render, redirect
from .utils import get_empresa_logada
from .models import Empresa, Produto, efetuar_login_empresa, efetuar_login_usuario

# Create your views here.
def cadastrar_empresa(request):
    if request.method == 'POST':
        dono_empresa = request.POST.get('dono_empresa')
        nome_empresa = request.POST.get('nome_empresa')
        faturamento = request.POST.get('faturamento')
        
        empresa = Empresa(
            dono_empresa = dono_empresa,
            nome_empresa = nome_empresa,
            faturamento = faturamento
        )
        empresa.save()
        
        request.session['empresa_logada_id'] = empresa.id
        
        return redirect('home')    
        
    return render(request, 'cadastrar_empresa.html')


def logar_empresa(request):
    
    if request.method == 'POST':
        dono_empresa = request.POST.get('dono_empresa')
        nome_empresa = request.POST.get('nome_empresa')
        
        empresa_logada = efetuar_login_empresa(dono_empresa, nome_empresa)
        
        if empresa_logada:
            request.session['empresa_logada_id'] = empresa_logada.id
            return redirect('home')    
        
    return render(request, 'logar_empresa.html')

def logar_usuario(request):
    if request.method == 'POST':
        # nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        usuario_logado = efetuar_login_usuario(email, senha)
        
        if usuario_logado:
            request.session['usuario_logado_id'] = usuario_logado.id
            return redirect('home')    
        
    return render(request, 'logar_usuario.html')


def perfil(request):
    empresa_logada = get_empresa_logada(request)
    
    context = {
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None
    }
    
    if request.method == 'POST':
        deslogar = request.POST.get('deslogar')
        
        if deslogar:
            request.session['empresa_logada_id'] = None
            return redirect('logar_empresa') 
    
    return render(request, 'profile.html', context)


def index(request):
    empresa_logada = get_empresa_logada(request)
    
    context = {
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None
    }
    
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        preco = request.POST.get('preco')
        
        btn_add = request.POST.get('btn_add')
        btn_remove = request.POST.get('btn_remove')
        
        if btn_add:
            produto = Produto(
                nome_produto = nome_produto,
                quantidade_estoque = quantidade_estoque,
                preco = preco
            )
            produto.save()
            empresa_logada.adicionar_produto(produto)
        
        if btn_remove:
            id_produto_escolhido = request.POST.get('produto_id')
            empresa_logada.remover_produto(id_produto_escolhido)
            print(f"Produto removido!")
    
    return render(request, 'auth_empresa.html', context)

def landing(request):
    empresa_logada = get_empresa_logada(request)
    # or usuario_logado is not None 
    
    context = {
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None 
    }
    
    return render(request, 'landing.html', context)