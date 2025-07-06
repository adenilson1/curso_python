# cvs.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DctReader lê o CSV em formato de dicionario

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula19.csv"

lista_clientes = [
    {"Nome": "Luiz Otávio", "Endereço": "Av 1, 22"},
    {"Nome": "João Silva", "Endereço": 'R. 2 , "1"'},
    {"Nome": "Maria Sol", "Endereço": "Av. B, 3A"},
]
# with open(CAMINHO_CSV, "w") as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for clientes in lista_clientes:
#         escritor.writerow(clientes.values())

# usando dicionario

with open(CAMINHO_CSV, "w") as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
