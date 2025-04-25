from django.shortcuts import render, redirect
from .models import Usuario
from empresas.utils import get_usuario_logado, efetuar_login_usuario

def logar_usuario(request):
    if request.method == 'POST':
        # nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        usuario_logado = efetuar_login_usuario(email, senha)
        
        if usuario_logado:
            request.session['usuario_logado_id'] = usuario_logado.id
            return redirect('landing')    
        
    return render(request, 'logar_usuario.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirm_senha')
        
        if confirm_senha == senha:
            usuario = Usuario(
                nome_completo = nome_completo,
                email = email,
                senha = senha
            )
            usuario.save()  
        
            request.session['usuario_logado_id'] = usuario.id
        
            return redirect('landing')    
        
    return render(request, 'cadastrar_usuario.html')