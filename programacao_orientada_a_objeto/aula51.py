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

from dataclasses import dataclass, field, fields


@dataclass(repr=True)
class Pessoa:
    nome: str = field(default="Maria", repr=False)
    sobrenome: str = "dalva"
    idade: int = 0  # valor imutavel
    endereco: list[str] = field(default_factory=list)


if __name__ == "__main__":
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)
