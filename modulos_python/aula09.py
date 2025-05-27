# os.listdir para navegar em caminhos
# /Users/ad/Área de trabalho/EXEMPLO
# caminho = "/home/ad/Área de trabalho/EXEMPLO"
import os

caminho = os.path.join("/home", "ad", "Área de trabalho", "EXEMPLO")

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(" ", imagem)
