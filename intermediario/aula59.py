#Problemas dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista = None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luis')
adiciona_clientes('joana', cliente1)
adiciona_clientes('fernando', cliente1)
cliente1.append('edu')


cleinte2 = adiciona_clientes('helena')
adiciona_clientes('maria',cleinte2)

cleinte3 = adiciona_clientes('Pedro')
adiciona_clientes('vitoria',cleinte3)

print(cliente1)
print(cleinte2)
print(cleinte3)