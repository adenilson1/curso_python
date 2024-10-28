"""
Criando argquivos com Python
Usamos a função open para abrir
um arquivo em Python (ele pode ou nao existir)
Modos:
r (leitura), w (escrita), x (criação), a (escrever ao final), b(binario)
t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)
Metodos uteis:
write, read, (escrever e ler)
writelines (escrever varias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
Vamos falar mais sobre o modulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome o move o arquivo
Vamos falar mais sovre o modulo json, mas:
json.dump = Gera um arquivo json
json.load
"""

caminho_arquivo = 'aula55.txt'
print(caminho_arquivo)

#arquivo = open(caminho_arquivo, 'w') 
#
#arquivo.close()

""""
with open (caminho_arquivo, 'w+') as arquivo:
    print(type(arquivo))
    arquivo.write('linha 1\r\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n','linha 4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())
    arquivo.seek(0,0)

print('#' * 40)

with open (caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
"""
with open (caminho_arquivo, 'w') as arquivo:
    print(type(arquivo))
    arquivo.write('linha 1\r\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n','linha 4\n')
    )