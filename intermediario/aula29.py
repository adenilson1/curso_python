"""
Valores Truthy e Falsy, tipos mutáveis e imutáveis
Mutávies -> [], {}, set()
IMutávies -> (), "", 0, 0.0, None, False range(0,10)
"""

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{dicionario}', falsy(dicionario))
print(f'{conjunto}', falsy(conjunto))
print(f'{tupla}', falsy(tupla))
print(f'{inteiro}', falsy(inteiro))
print(f'{flutuante}', falsy(flutuante))
print(f'{nada}', falsy(nada))
print(f'{falso}', falsy(falso))
print(f'{intervalo}', falsy(intervalo))