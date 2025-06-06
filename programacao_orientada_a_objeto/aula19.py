# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem 
# Composição - É dono de, Herança - É um

# Herança ou Composição

# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Clientes)
# -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('CLASSE PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('NEM SAI DO CLASSE CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...
    


c1 = Cliente('Adenilson', 'Lima')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Lima')
a1.falar_nome_classe()
print(a1.cpf)

#help(Cliente)
    
