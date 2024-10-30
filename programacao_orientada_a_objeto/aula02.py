
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome




p1 = Pessoa('Adenilson', 'Diniz')
# p1.nome = 'Adenilson'
# p1.sobrenome = 'Diniz'

p2 = Pessoa('Maria', 'Joanna')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joanna'


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)