
import enum


# Direcoes = enum.Enum('Direcoes',['ESQUERDA', 'DIREITA'])
# print(Direcoes(1),Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
# print(Direcoes(1).name,Direcoes.ESQUERDA.value)

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção nao encontrada')

        

    print(f'Movendo para {direcao.name} ({direcao.value})')




mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)

