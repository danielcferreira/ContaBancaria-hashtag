# 1 comecar toda classe sempre com letra maiuscula
# 2 - Uma linha de espaço entre os metodos - funcao
# 3 - Uma metodo para cada coisa 
# 4 - todos os atributos devem estar no metodo/funcao init 
# 5 - 

class ContaCorrente:

    # 12 - criando sistema de conta Corrente
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo =  0
        self.limite = None

    # 13 - criando metodos para a classe
    def consultar_saldo(self):
        return print(f'seu saldo atual e de R${self.saldo:,.2f}')

    def deposito(self, valor):
        self.saldo += valor
        return print(f'seu deposito de R${self.saldo:,.2f}')
    
    # aula 14 - metoddo auxiliar - metodo privado
    def _limite_conta(self):
        self.limite = -1000
        return self.limite
    
     # aula 14 - metoddo auxiliar - metodo privado
    def _analisa_limite(self):
        if self.saldo < 0:
           print('####---- voce esta no cheque especial ----#####')
           return  print(f'seu saldo atual e de R${self.saldo:,.2f} do limite de R${self.limite:,.2f}')
            
    def saque(self, valor):
        if self.saldo - valor >= self._limite_conta():
            self.saldo -= valor
            print(f'voce sacou {valor:,.2f}')
            self._analisa_limite() 
        else:
            print('voce nao tem saldo')


    def consultar_limite_chequeEspecial(self):
        if self.saldo < 0:
            #print(f'Seu limite de cheque especial e de R${self._limite_conta():,.2f}')
            print(f'seu saldo atual e de R${self.saldo:,.2f} do limite de R${self.limite:,.2f}')
        else:
            print(f'seu e de limite de R${self.limite:,.2f}')

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

conta_daniel.consultar_saldo()
conta_daniel.saque(1000)
#conta_daniel.saque(63)

conta_daniel.consultar_limite_chequeEspecial()
