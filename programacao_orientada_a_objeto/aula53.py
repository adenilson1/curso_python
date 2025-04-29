"""
Implementando o protocolo do iterator em Python
Essa é apenas uma uala para introduzir os protocolos de
colletions. abc no Python.
Qualquer outro protocolo poderá ser implementado seguindo
a mesma estrutura usada nessa aula

"""

from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):

        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __setitem__(self, index, value):
        self._data[index] = value

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return self

    def __next__(self):

        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == "__main__":
    lista = MyList()
    lista.append("Maria", "Helena")
    lista[0] = "João"
    lista.append("Luis")
    # print(lista[0])
    # print(len(lista))

    for item in lista:
        print(item)

    print("--------")

    for item in lista:
        print(item)
