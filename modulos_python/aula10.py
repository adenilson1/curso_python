# os.walk
# os.walk é uma função que paermite percorrer uma estrutura de diretorios
# de maneira recursiva. Ela gera uma sequencia de tuplas, onde cada tupla possui
# tres elementos: o diretorio autla(root), uma lista de subdiretorios(dirs)
# e uma lista dos arquivos do diretorio atual(files)

import os
from itertools import count

counter = count()
caminho = os.path.join("/home", "ad", "Área de trabalho", "EXEMPLO")

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, "Pasta atual", root)

    for dir_ in dirs:
        print(" ", the_counter, "Dir ", dir_)

    # for file_ in files:
    #     print(" ", the_counter, "File ", file_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print(" ", the_counter, "FILE", caminho_completo_arquivo)
        os.unlink(caminho_completo_arquivo)
