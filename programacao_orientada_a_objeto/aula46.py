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


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == "__main__":
    p1 = Pessoa("Luiz", 30)
    p2 = Pessoa("Luiz", 30)
    print(p1 == p2)
