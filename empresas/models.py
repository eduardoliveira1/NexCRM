from django.db import models


class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, default='produto')
    quantidade_estoque = models.IntegerField(default=0)
    preco = models.FloatField(default=0)

class Empresa(models.Model):
    dono_empresa = models.CharField(max_length=150, default='dono da empresa')
    nome_empresa = models.CharField(max_length=80, unique=True)
    faturamento = models.FloatField(default=0)
    produtos = models.ManyToManyField(Produto)
    
    def adicionar_produto(self, produto:Produto):
        self.produtos.add(produto)
        self.save()
        
    def remover_produto(self, id_produto_escolhido):
        produto = self.produtos.filter(id=id_produto_escolhido).first()
        if produto:
            self.produtos.remove(produto)
            self.save()

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=200, default='usuario')
    email = models.EmailField(default='usuario@gmail.com')
    senha = models.CharField(max_length=20, default='senha')
    saldo = models.FloatField(default=0)
    produtos_comprados = models.ManyToManyField(Produto)
    
    def comprar_produto(self, empresa, id_produto, quantidade):
        empresa = Empresa.objects.get(nome_empresa=empresa)
        produto = Produto.objects.get(id=id_produto)
        
        if empresa:
            if produto:
                if self.saldo >= produto.preco*quantidade:
                    empresa.faturamento += produto.preco * quantidade
                    produto.quantidade_estoque -= quantidade
                    self.produtos_comprados.add(produto)
            
            
def efetuar_login_empresa(dono_empresa, nome_empresa):
    empresa = Empresa.objects.get(nome_empresa=nome_empresa)
    if empresa:
        if dono_empresa == empresa.dono_empresa:
            return empresa 
    return None 

def efetuar_login_usuario(email, senha):
    usuario = usuario.objects.get(email=email)
    if usuario:
        if senha == usuario.senha:
            return usuario 
    return None