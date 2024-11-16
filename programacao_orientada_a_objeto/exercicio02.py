# Exercicio com classes
# 1- Crie uma classe Carro(nome)
# 2- Crie uma classe Motor(nome)
# 3- Crie uma classe Fabricante(nome)
# 4- Faça a ligação entre Carro tem Motor 
# Obs.: Um motor pode ser de varios carros
# 5- Faça a lisgação entre Carro e Fabricante
# Obs.: Um Fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e Fabricante na tela.

class Carro:
    def __init__(self, nome_carro):
        self.nome_carro= nome_carro
        self._motor = None
        self._fabricante = None

    
    @property
    def motor_de_carro(self):
        return self._motor
    
    @motor_de_carro.setter
    def motor_de_carro(self, motor):
        self._motor = motor


    @property
    def fabricante_de_carro(self):
        return self._motor
    
    @fabricante_de_carro.setter
    def fabricante_de_carro(self, fabrica):
        self._fabricante = fabrica


class Motor:
    def __init__(self, tipo_motor):
        self.tipo_motor = tipo_motor

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante



c1 = Carro('Uno')
c1.motor = Motor('1.0')
c1.fabricante = Fabricante('Fiat')
print(c1.nome_carro, c1.motor.tipo_motor, c1.fabricante.nome_fabricante)

c2 = Carro('Palio')
c2.motor = Motor('2.0')
c2.fabricante = Fabricante('Fiat')
print(c2.nome_carro, c2.motor.tipo_motor, c2.fabricante.nome_fabricante)

c3 = Carro('Gol')
c3.motor = Motor('2.0')
c3.fabricante = Fabricante('volkswagen')
print(c3.nome_carro, c3.motor.tipo_motor, c3.fabricante.nome_fabricante)



    