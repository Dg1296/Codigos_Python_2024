import streamlit as st 

class ContaBancaria:
    def __init__(self,numero_conta,saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def depositar(self,valor):
        if valor > 0 :
            self.saldo += valor
        else:
            print('O valor nao pode ser negativo!')
    
    def sacar(self,valor):
        if self.saldo > valor and valor > 0:
            self.saldo -= valor 
        else:
            print('Saldo insuficiente!')
    
    def transferir(self,conta_destino,valor):
        if self.saldo > valor:
            self.saldo -= valor
            conta_destino.depositar(valor)
        else:
            print('Saldo insuficiente')
    
    def exibir_saldo(self,numero_conta):
        print(f'Conta: {numero_conta} saldo: {self.saldo} ')
            
class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome 
        self.cpf = cpf

class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = {}
        
    def cadastrar_cliente(self,nome,cpf):
        if cpf not in self.clientes:
            self.clientes[cpf] = Cliente(nome,cpf)
            print(f'Cliente cadastrado com sucesso! Nome: {nome} CPF: {cpf}')
        else:
            print(f'CPF: {cpf} ja cadastrado!')
            
    def abrir_conta(self,cpf,numero_conta):
        if cpf in self.clientes:
            if numero_conta not in self.contas:
                self.contas[numero_conta] = ContaBancaria(numero_conta)
                print(f'Conta {numero_conta} cadastrada com sucesso!')
            else:
                print(f'Numero de conta {numero_conta} ja cadastrado!')
        else: 
            print(f'CPF: {cpf} nao cadastrado!')
    
    def realizar_deposito(self,numero_conta,valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].depositar(valor)
            print(f'Deposito realizado na conta: {numero_conta} valor: R$: {valor}')
        else: 
            print(f'Numero de conta {numero_conta} nao encontrado!')
    
    def realizar_saque(self,numero_conta,valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].sacar(valor)
            print(f'Saque realizado com sucesso na conta {numero_conta} valor: R$: {valor}')
        else:
            print(f'Numero da conta {numero_conta} nao encontrada!')
    
    def realizar_tranferencia(self,conta_origem,conta_destino,valor):
        if conta_origem in self.contas and conta_destino in self.contas:
            self.contas[conta_origem].transferir(self.contas[conta_destino],valor)
            print(f'Valor R$: {valor} transferido com sucesso! de conta: {conta_origem} para {conta_destino}')
        else:
            print(f'Conta de origem ou destino nao encotrada!')
    
    def apresentar_saldo(self,numero_conta):
        if numero_conta in self.contas:
            self.contas[numero_conta].exibir_saldo(numero_conta)


            
        
    