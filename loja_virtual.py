class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome =  nome 
        self.preco = preco
        self.quantidade = quantidade
        
class LojaVirtual:
    def __init__(self):
        self.produtos = {}
        self.carrinho = {}
        
    def cadastrar_produto(self,produto):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade += produto.quantidade
            print(f'{produto.nome} quantidade alterada.')
        else:
            self.produtos[produto.nome] = produto
            print(f'{produto.nome} adicionado {produto.quantidade} unidade(s) ao estoque.')
    
    def adicionar_ao_carrinho(self,nome_produto,quantidade):
        if nome_produto in self.produtos and self.produtos[nome_produto].quantidade >= quantidade:
            if nome_produto in self.carrinho:
                self.carrinho[nome_produto] += quantidade
                print('quantidade alterada no carrinho')
            else:
                self.carrinho[nome_produto] = quantidade
            self.produtos[nome_produto].quantidade -= quantidade
            print(f'{nome_produto} adicionado {quantidade} unidade(s) ao carrinho.')
        else:
            print(f'{nome_produto} nao encontrado ou sem estoque disponivel.')
    
    def aplicar_desconto(self,desconto):
        for nome_produto in self.carrinho:
            produto = self.produtos[nome_produto]
            produto.preco -= produto.preco * (desconto/100)
        print(f'Desconto de {desconto}% adicionado')
    
    def calcular_valor_total(self):
        total = 0 
        for nome_produto , quantidade in self.carrinho.items():
            total += self.produtos[nome_produto].preco * quantidade
        return total
    
    def exibir_carrinho(self):
        if not self.carrinho:
            print('Carrinho vazio !')
            return
        print('Carrinho de compras:')
        for nome_produto , quantidade in self.carrinho.items():
            produto = self.produtos[nome_produto]
            print(f'{produto.nome} - {quantidade} unid - {produto.preco:.2f} cada')
        total = self.calcular_valor_total()
        print(f'Total dos produtos no carrinho: R$: {total}')
            
                    
        


loja = LojaVirtual()

iphone_13 = Produto('Iphone 13',5000,2)
xiaomi = Produto('Note 13',2400,3)

loja.cadastrar_produto(iphone_13)
loja.cadastrar_produto(xiaomi)
print('\n')
loja.adicionar_ao_carrinho('Iphone 13',1)
loja.adicionar_ao_carrinho('Note 13',1)
print('\n')

loja.aplicar_desconto(10)

loja.exibir_carrinho()