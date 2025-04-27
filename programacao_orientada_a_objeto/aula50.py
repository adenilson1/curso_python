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

from dataclasses import dataclass, asdict, astuple

# asdict -> converte uma tupla para dicionario
# astuple -> converte um dicionario para uma tupla


@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == "__main__":
    p1 = Pessoa("Luiz", "Otávio")
    print(asdict(p1))
    print(astuple(p1))

    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())

    print(astuple(p1)[0])
