# os.path trabalha com caminhso em Windows, Linux e Mac
# os.path é um módulo que fornece para trabalhar com caminhos de
# arquivos em Windows, Mac e Linux sem precisar se preocupar com as
# diferenças entre sistemas.
# Exemplo do os.path:
# os.path.join: junta strings em um único caminho. Desse modo, os.path.join
# ('pasta1', 'pasta2', 'arquivo.text') retornaria
# 'pasta1/pasta2/arquivo.text' no linux
# 'pasta1\pasta2\arquivo.text' no Windows # type: ignore
# os.path.split: divide um caminho uma tupla (diretorio, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.text')
# retornaria ('/home/user', 'arquivo.text').
# os.path.exists: verifica se um caminho específico existe
# os.path so trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrad/saida (I/O) com arquivos em si.

import os

caminho = os.path.join("Desktop", "curso", "arquivo.text")
# print(caminho)
print(os.path.split(caminho))
print(80 * "_")
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(arquivo)
print(nome_arquivo, extensao_arquivo)
print(80 * "_")
print(os.path.exists(caminho))
print(os.path.exists("/home/ad/Área de trabalho/curso_python"))
print(80 * "_")
print(os.path.abspath("."))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))
