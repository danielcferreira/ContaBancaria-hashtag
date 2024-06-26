#indice
# 06 - o que é uma classe
# 07 - o que é o self
# 08 - Criando metodo dentro da classe 
# 09 - parametros nos metodos e na classe
# 10 - Parâmetros no init da Classe 
# 11 - atributos de classe


class TV:
    # atributos de classe
    cor = preta 


    # metod é uma funcao 
    # depois de cria a class criar a funcao init para iniciar a classe

    def __init__(self, tamanho):
    # aquiser são os atributos da funca que podem ser mudados
        self.cor = 'preta'
        self.ligado = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10
    # o que é o self ? 
    #  seu quer dizer ele mesmo, e um paramentro que remeta a propria classe tv 
    # é ele quem permite que possa acessar a classe fora dela, semque quiser 
    # acessar um parametro da classe deve se usar o self na frente

    # criando um metodo
    def mudar_canal(self, novo_canal):
        self.canal =  novo_canal

tv_sala = TV(22)
tv_quarto = TV(30)

# posso mudar os atributos
'''
aula - o que é o self
tv_quarto.cor = 'branca'
print(tv_quarto.cor)
print(tv_sala.volume)
'''

# se tiver () esta usando metodo 
tv_sala.mudar_canal('globo')
tv_quarto.mudar_canal('discovery chanel')

# sem () esta usando um atributo
print(tv_sala.canal)
print(tv_quarto.canal)

# tv tamanho
print(tv_sala.tamanho)

    