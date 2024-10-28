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

caminho_arquivo = '/home/ad/Área de trabalho/python/intermediario/'
caminho_arquivo += 'aula54.txt'
print(caminho_arquivo)

#arquivo = open(caminho_arquivo, 'w') 
#
#arquivo.close()

with open (caminho_arquivo, 'w') as arquivo:
    print('Olá mundo!!!!')
    print('Arquivo vai ser fechado')