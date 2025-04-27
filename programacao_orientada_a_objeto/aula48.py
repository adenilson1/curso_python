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


@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    def __post_init__(self):
        print("Pós __init__")

    # @property
    # def nome_completo(self):
    #     return f"{self.nome} {self.sobrenome}"

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = " ".join(" ")


if __name__ == "__main__":
    p1 = Pessoa("Luiz", "Otávio")
    print(p1)
    print(p1.nome_completo)
