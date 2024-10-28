import os

caminho_arquivo = 'aula57.txt'


with open (caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('linha 1\r\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n','linha 4\n')
    )
#os.unlink(caminho_arquivo) # remove arquivo
#os.unlink(caminho_arquivo) # remove arquivo

