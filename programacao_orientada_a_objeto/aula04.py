# Entendo self em classes Python
# Classe -> é um molde (geralmente sem dados)
# Instancia da class (objeto) -> tem os dados
# Uma classe pode gerar vairias instancias
# Na classe pode gerar varias instancias
# self -> server para referenciar a propria instancia 
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando ...')



fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()