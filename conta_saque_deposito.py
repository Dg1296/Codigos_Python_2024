class Cliente:
    def __init__(self,nome,cpf,telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        
class Conta(Cliente):
    def __init__(self,nome, cpf, telefone,numero_conta):
        super().__init__(nome, cpf, telefone)
        self.num_conta = numero_conta
        self.saldo = 0
     
    def realizar_deposito(self,numero_conta,deposito):
        if self.num_conta != numero_conta:
            raise ValueError('Essa conta nao existe')
        if deposito < 0:
                raise ValueError('O valor nao pode ser negativo!')
        self.saldo += deposito
        
    def sacar_dinheiro(self,saque):
        if self.saldo < saque:
            raise ValueError('Voce nao tem esse saldo!!')
        self.saldo -= saque
    
    @property
    def dados_conta_cliente(self):
        return f'---- DADOS CLIENTE ---- \n Nome Cliente: {self.nome} CPF: {self.cpf} Telefone: {self.telefone} \n N. Conta: {self.num_conta}   ---- SALDO: {float(self.saldo)} ----'
        
if __name__ == '__main__':         
    cliente1 = Cliente('Douglas Ferreira','05918144129','333567667')        
    conta1 = Conta(cliente1.nome , cliente1.cpf , cliente1.telefone , '1111-11')
    conta1.realizar_deposito('1111-11',2000)
    conta1.realizar_deposito('1111-11',123.55)
    print(conta1.dados_conta_cliente)
    cliente2 = Cliente('Diego Ferreira','05533344554', '944544455')
    conta2 = Conta(cliente2.nome , cliente2.cpf , cliente2.telefone , '2222-22')
    conta2.realizar_deposito('2222-22',5000)
    print(conta2.dados_conta_cliente)
   

