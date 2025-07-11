# csv.reader e csv.DictReader
# csv.raeder lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula18.csv"

with open(CAMINHO_CSV, "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

with open(CAMINHO_CSV, "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["Nome"], linha["Idade"], linha["Endereço"])
