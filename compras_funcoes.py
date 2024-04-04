class Produto:
    def __init__(self,nome,valor,quant):
        self.nome = nome
        self.valor = valor 
        self.quant = quant
        
class Cliente:
    def __init__(self,nome,cpf,telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        

class Compra:
    def __init__(self):
        self.cliente = []
        self.lista = []
        
    def add_produto(self,nome,valor,quant):
        self.lista.append(Produto(nome,valor,quant))
        
    def add_cliente(self,nome,cpf,telefone):
        self.cliente.append(Cliente(nome,cpf,telefone))
        
    def procurar_produto(self,nome):
        return[produto for produto in self.lista if produto.nome == nome][0]
    
    def exibir_produtos(self):
        for produ in self.lista:
              print(f'Produto: {produ.nome} Qtd: {produ.quant} Valor: {produ.valor}')
    
    def valor_total(self):
        total = 0
        for vl in self.lista:
            total += vl.valor * vl.quant
        return total

    def __str__(self):
        for cl in self.cliente:
            return f'----- DADOS CLIENTE ----- \n Nome: {cl.nome} \n CPF: {cl.cpf} \n TEL: {cl.telefone}'
    

if __name__ == '__main__':
    compra1 = Compra()
    compra1.add_cliente('Douglas Ferreira','059.181.441-29','61 994453346')
    compra1.add_produto('Iphone 15 128gb',3000,2)
    compra1.add_produto('Xiaomi Note 13',1750,3)
    print(compra1,'\n')
    compra1.exibir_produtos()
    print('\n')
    print(f'Valor Total: {compra1.valor_total()}')
    
    
    
    
    