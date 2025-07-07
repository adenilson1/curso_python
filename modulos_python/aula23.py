# string.Template para substituir variáveis em textos
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerear erros
# Você também pode trocar o delimitador e outros criando uma subclasse
# de template.
import string
import locale
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "aula23.txt"

locale.setlocale(locale.LC_ALL, "")


def converte_para_br1(numero: float) -> str:
    br1 = "R$ " + locale.currency(val=numero, symbol=False, grouping=True)
    return br1


data = datetime(2022, 12, 28)
dados = dict(
    nome="João",
    valor=converte_para_br1(1_123_456),
    data=data.strftime("%d/%m/%Y"),
    empresa="O. M.",
    telefone="+55 (11) 7890-5432",
)


with open(CAMINHO_ARQUIVO, "r") as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
