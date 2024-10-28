
caminho_arquivo = 'aula56.txt'


with open (caminho_arquivo, 'w') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('linha 1\r\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n','linha 4\n')
    )