import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # se o tamanho for meno ou igual 0,0 B
    if tamanho_em_bytes <= 0:
        return "0B"

    # tupla com os tamanhos
    # 0 1 2 3 4 5

    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    # math.log vai retorna o algoritmo do tamanho_em_bytes
    # com base (1024 por padrao), isso deve bater
    # com o nosso indice na abreviaçao dos tamanho

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    # Por em quanto nosso tamanho deve ser dividico para
    # gerar o tamanho correto

    potencia = base**indice_abreviacao_tamanhos

    # Tamanho final

    tamanho_final = round(tamanho_em_bytes / potencia, 2)

    # Abreviação que queremos

    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f"{tamanho_final} {abreviacao_tamanho}"


counter = count()
caminho = os.path.join("/home", "ad", "Área de trabalho", "EXEMPLO")

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, "Pasta atual", root)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print(" ", the_counter, "FILE", file_, formata_tamanho(tamanho))
        # os.unlink(caminho_completo_arquivo)
