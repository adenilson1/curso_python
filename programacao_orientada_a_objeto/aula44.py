"""
Enum > Enumeração
Enumeração na programação, são usadas em ocasioões 
em termos onde temos um determinado número de coisas
Enums têm membros e seus valores são constantes.
Enums em python:
    São um conjunto de nomes simbólicos (membros)
    ligados a valores unicos
    podem ser iterados para retornar seus membros canonicos 
    na ordem de definição

enum. Enum é a superclasse para usa senumerações, mas pode 
ser usadas diretamete (mesmo assim, Enums não são classes
normais em python)
Poderá se usar o Enum com type annotations, com isintance  e
outas coisas relacionadas com tipo

dados:
chave = Classe.chave.nome, Classe(valor), Classe['chave]
valor = Classe.chave.value

"""

def mover(direcao):
    print(f'Movendo para {direcao}')

mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')