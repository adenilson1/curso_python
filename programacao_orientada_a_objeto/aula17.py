# Relação entre classes: associação, agregação e composição
# Composicão é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as refrencias dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO, ', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO, ', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av.Brasil',54)
cliente1.inserir_endereco('Rua B',45)
cliente1.listar_enderecos()


print('##################AQUI TERMINA MEU CODIGO')