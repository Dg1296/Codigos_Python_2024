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
        
    def add_produto(self,nome=None,valor = 0 , quant = 0):
        
        while True:
            nome = input('Nome produto: ')
            valor = int(input('Valor do produto: '))
            quant = int(input('QTD Produto: '))
            self.lista.append(Produto(nome,valor,quant)) 
            confirme = input('Deseja inserir novo produto? [S\ N]')
            if confirme == 'n':
                break
            else:'\n'
                 
    def add_cliente(self):
        nome = input('Nome cliente: ')
        cpf = input('CPF: ')
        telefone = input('Telefone: ')
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
    
def main():
    compra1 = Compra()
    compra1.add_cliente()
    compra1.add_produto()
    print('\n \n')
    print(compra1)
    compra1.exibir_produtos()
    print(compra1.valor_total())
    
main()
    
    
    
