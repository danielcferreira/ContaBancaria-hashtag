class ContaCorrente:

    # 12 - criando sistema de conta Corrente
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo =  0

    # 13 - criando metodos para a classe
    def consultar_saldo(self):
        return print(f'seu saldo atual e de R${self.saldo:,.2f}')

    def deposito(self, valor):
        self.saldo += valor
        return print(f'seu deposito de R${self.saldo:,.2f}')
    
    def saque(self, valor):
        if self.saldo - valor < 0:
            self.saldo -= valor
            return print(f'voce sacou {valor} saldo atual é de R${self.saldo:,.2f}')
        else:
            print('voce nao tem saldo')

    def extrato():
        pass

 

    def transferencia():
        pass



# Programa
conta_daniel = ContaCorrente('daniel','123456789')
conta_marta =  ContaCorrente('Marta','987456123')

print(conta_daniel.cpf)
conta_daniel.saldo = 63
conta_daniel.consultar_saldo()

conta_daniel.deposito(6000)
conta_daniel.saque(3500)
conta_daniel.saque(2500)
conta_daniel.saque(70)