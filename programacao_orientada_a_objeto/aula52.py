"""
namedtuples - tuplas imutáveis com nome para valores
Usamos namedtuples para criar classes de objetos que
são apenas um agrupamento de atribuotos, como classes normais
sem métodos, ou registros de bases de dados, etc.
As namedtuples são imutáveis assim como as tuplas.

"""

# from collections import namedtuple

from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = "VALOR"
    naipe: str = "NAIPE"


# Carta = namedtuple("Carta", ["valor", "naipe"], defaults=["VALOR", "NAIPE"])
as_espadas = Carta("A")

print(as_espadas._asdict())
print(as_espadas)
print(as_espadas.naipe)
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])

print("##########")

print(as_espadas._fields)
print(as_espadas._field_defaults)


for valor in as_espadas:
    print(valor)
