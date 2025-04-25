from django.db import models
from empresas.models import Produto

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=200, default='usuario')
    email = models.EmailField(default='usuario@gmail.com')
    senha = models.CharField(max_length=20, default='senha')
    produtos_comprados = models.ManyToManyField(Produto, related_name='produtos_comprados', blank=True)
    
    def comprar_produto(self, produto:Produto, quantidade:int):
        quantidade = int(quantidade)
        if quantidade >= 1 and quantidade <= produto.quantidade_estoque:
            produto.empresa.faturamento += produto.preco * quantidade
            produto.quantidade_estoque -= quantidade
            self.produtos_comprados.add(produto)
            produto.save()
            produto.empresa.save()
            self.save()
            
    def editar_email(self, novo_email):
        self.email = novo_email
        self.save()
        