class Item:
    def __init__(self,nome,preco,quantidade = 1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def __str__(self):
        return f'{self.nome} = R${self.preco} X {self.quantidade}'
    
    def atualizar_quantidade(self,quantidade):
        self.quantidade += quantidade

class CarrinhoCompras:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self,item):
        for i in self.itens:
            if i.nome == item.nome:
                i.atualizar_quantidade(item.quantidade)
                break
        else:
            self.itens.append(item)
        print(f'{item} adiconado com sucesso !')
            
    def remover_item(self,nome_item):
        for item in self.itens:
            if item.nome == nome_item:
                self.itens.remove(item)
                print(f'{nome_item} removido com sucesso !')
                return
        else:
            print(f'{nome_item} nao encotrado !')
    
    def exibir_carrinho(self):
        if not self.itens:
            print('Carrinho vazio !')
            return
        print('Carrinho de compras:')
        for item in self.itens:
            print(f'- {item}')
        total = sum(item.preco * item.quantidade for item in self.itens)
        print(f'Total: R$ {total}')
        
carrinho = CarrinhoCompras()

iphone_15 = Item('Iphone 15',7000,1)
iphone_14 = Item('Iphone 14',6000,1)
iphone_13 = Item('Iphone 13',5000,1)

carrinho.adicionar_item(iphone_15)
carrinho.adicionar_item(iphone_14)
carrinho.adicionar_item(iphone_13)

carrinho.exibir_carrinho()

carrinho.remover_item('Iphone 13')

carrinho.exibir_carrinho()


    
        
            