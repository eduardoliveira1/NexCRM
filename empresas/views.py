from django.shortcuts import render, redirect
from .utils import get_empresa_logada, get_usuario_logado, efetuar_login_empresa, get_produto_escolhido
from .models import Empresa, Produto
from django.contrib import messages
from usuarios.models import Usuario

# Create your views here.
def cadastrar_empresa(request):
    if request.method == 'POST':
        dono_empresa = request.POST.get('dono_empresa')
        nome_empresa = request.POST.get('nome_empresa')
        
        empresa = Empresa(
            dono_empresa = dono_empresa,
            nome_empresa = nome_empresa
        )
        empresa.save()
        
        request.session['empresa_logada_id'] = empresa.id
        
        return redirect('landing')    
        
    return render(request, 'cadastrar_empresa.html')

def logar_empresa(request):
    
    if request.method == 'POST':
        dono_empresa = request.POST.get('dono_empresa')
        nome_empresa = request.POST.get('nome_empresa')
        
        empresa_logada = efetuar_login_empresa(dono_empresa, nome_empresa)
        
        if empresa_logada:
            request.session['empresa_logada_id'] = empresa_logada.id
            return redirect('landing')    
        
    return render(request, 'logar_empresa.html')

def perfil(request):
    empresa_logada = get_empresa_logada(request)
    usuario_logado = get_usuario_logado(request)
    
    
    context = {
        'usuario_logado' : usuario_logado,
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None or usuario_logado is not None 
    }
    
    if request.method == 'POST':
        deslogar = request.POST.get('deslogar')
        novo_dono_empresa = request.POST.get('dono_empresa')
        novo_nome_empresa = request.POST.get('nome_empresa')
        novo_email = request.POST.get('novo_email')
        
        if novo_dono_empresa:
            empresa_logada.editar_dono_empresa(novo_dono_empresa)
        if novo_nome_empresa:
            empresa_logada.editar_nome_empresa(novo_nome_empresa)
        if novo_email:
            usuario_logado.editar_email(novo_email)
        
        if deslogar:
            request.session['empresa_logada_id'] = None
            request.session['usuario_logado_id'] = None
            return redirect('landing') 
    
    return render(request, 'profile.html', context)

def cadastrar_produtos(request):
    empresa_logada = get_empresa_logada(request)
    usuario_logado = get_usuario_logado(request)
    
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        preco = request.POST.get('preco')
        
        produto_id = request.POST.get("produto_id")
        novo_nome = request.POST.get("novo_nome_produto")
        nova_quantidade = request.POST.get("nova_quantidade")
        novo_preco = request.POST.get("novo_preco")

        produto_escolhido = Produto.objects.filter(id=produto_id).first()

        if produto_escolhido:
            if novo_nome:
                produto_escolhido.editar_nome_produto(novo_nome)
                # messages.info(request, f"Produto editado com sucesso!")
            if nova_quantidade:
                produto_escolhido.editar_quantidade_estoque(nova_quantidade)
            if novo_preco:
                produto_escolhido.editar_preco(novo_preco)
        else:
            print(f"nao encontramos o produto")
        
        btn_add = request.POST.get('btn_add')
        btn_remove = request.POST.get('btn_remove')
        
        if btn_add:
            produto = Produto(
                nome_produto = nome_produto,
                quantidade_estoque = quantidade_estoque,
                preco = preco,
                empresa=empresa_logada
            )
            produto.save()
            empresa_logada.adicionar_produto(produto.id)
        
        if btn_remove:
            id_produto_escolhido = request.POST.get('produto_id')
            produto = Produto.objects.filter(id=id_produto_escolhido, empresa=empresa_logada).first()
            if produto:
                empresa_logada.remover_produto(id_produto_escolhido)
    
    context = {
        'usuario_logado' : usuario_logado,
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None or usuario_logado is not None 
    }
    
    return render(request, 'produtos_empresa.html', context)

def ver_produtos(request):
    empresa_logada = get_empresa_logada(request)
    usuario_logado = get_usuario_logado(request)
    catalogo = Produto.objects.all()
    
    context = {
        'catalogo' : catalogo,
        'usuario_logado' : usuario_logado,
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None or usuario_logado is not None 
    }
    
    if request.method == 'POST':
        btn_ver_produto = request.POST.get('btn_ver_produto')
        produto_id = request.POST.get('id_produto')
        produto = Produto.objects.get(id=produto_id)
        
        if produto and btn_ver_produto:
            request.session['produto_escolhido_id'] = produto.id
            return redirect('detalhes_produto')
    
    return render(request, 'ver_produtos.html', context)

def landing(request):
    empresa_logada = get_empresa_logada(request)
    usuario_logado = get_usuario_logado(request)
    
    context = {
        'usuario_logado' : usuario_logado,
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None or usuario_logado is not None 
    }
    
    return render(request, 'landing.html', context)

def produtos_comprados(request):
    empresa_logada = get_empresa_logada(request)
    usuario_logado = get_usuario_logado(request)
    
    context = {
        'usuario_logado' : usuario_logado,
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None or usuario_logado is not None 
    }
    return render(request, 'produtos_comprados.html', context)

def detalhes_produto(request):
    empresa_logada = get_empresa_logada(request)
    usuario_logado = get_usuario_logado(request)
    produto_escolhido = get_produto_escolhido(request)
    
    context = {
        'usuario_logado' : usuario_logado,
        'produto_escolhido' : produto_escolhido,
        'empresa_logada' : empresa_logada,
        'autenticado' : empresa_logada is not None or usuario_logado is not None 
    }
    
    if request.method == 'POST':
        btn_comprar = request.POST.get('btn_comprar')
        quantidade = request.POST.get('quantidade')
        
        if btn_comprar and usuario_logado:
            usuario_logado.comprar_produto(produto_escolhido, quantidade)
    
    return render(request, 'detalhes_produto.html', context)