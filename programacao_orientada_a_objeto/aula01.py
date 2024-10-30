# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instancias) que
# podem ter sues proprios atributos e metodos.
# Os objetos gerados pela classe podem usar seus dados 
# internos para realizar varias ações.
# Por convenção, usamos PascalCase para nome de classes.

# string = 'Adenilson' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Adenilson'
p1.sobrenome = 'Diniz'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joanna'


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)