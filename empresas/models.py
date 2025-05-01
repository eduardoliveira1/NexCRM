from django.db import models

    
class Empresa(models.Model):
    dono_empresa = models.CharField(max_length=150, default='dono da empresa')
    nome_empresa = models.CharField(max_length=80, unique=True)
    faturamento = models.FloatField(default=0)
    imagem_perfil = models.ImageField(upload_to='empresas_perfil/', default="empresas_perfil/empresa.jpeg")
        
    def remover_produto(self, id_produto):
        produto = Produto.objects.filter(id=id_produto, empresa=self).first()
        if produto:
            produto.delete() 
            
    def editar_dono_empresa(self, novo_nome):
        self.dono_empresa = novo_nome
        self.save()
        
    def editar_nome_empresa(self, novo_nome):
        self.nome_empresa = novo_nome
        self.save()
        
    def mudar_foto_perfil(self, nova_imagem):
        self.imagem_perfil = nova_imagem
        self.save()

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, default='produto')
    quantidade_estoque = models.IntegerField(default=0)
    preco = models.FloatField(default=0)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, related_name='produtos') 
    imagem_src = models.ImageField(upload_to='produtos/', default="produtos/cart.png")
    descricao = models.TextField(null=True, blank=True)

    def editar_nome_produto(self, novo_nome):
        self.nome_produto = novo_nome
        self.save()
        
    def mudar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
        self.save()
        
    def editar_quantidade_estoque(self, novo_estoque):
        quantidade = int(novo_estoque)
        if quantidade >= 0:
            self.quantidade_estoque = novo_estoque
            self.save()
        
    def editar_preco(self, novo_preco):
        self.preco = novo_preco
        self.save()
        
    def mudar_imagem(self, caminho_imagem):
        self.imagem_src = caminho_imagem
        self.save() 
