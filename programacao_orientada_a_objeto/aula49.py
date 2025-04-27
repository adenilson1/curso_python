"""
dataclasses  - o que são dataclasses?
O módulo dataclasses fornece um decorador e funções para
criar métodos como __init__(), __repr__(),
__eq__() (entre outros) em classes definidas pelo
usuário.
Em resumo: dataclasses são syntax sugar criar classes
normais.
Foi descrito na PEP 557 e adicionada na vesão 3.7 do
Python
"""

from dataclasses import dataclass

"""
nota: é sempre melhor criar uma nova variável,
do que alterar uma variável existente. isso é uma
boa pratica.
"""


@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == "__main__":
    lista = [Pessoa("A", "Z"), Pessoa("B", "Y"), Pessoa("C", "X")]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
