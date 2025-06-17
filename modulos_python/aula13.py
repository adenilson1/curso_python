# os+shutil - Apagando, copiando, movendo e renomeando pastas
# copiar -> shutil.copy
# Apagar Arvore recursivamente -> shutil.copytree
# Apagar arquivos -> os.unlink
# Renomear/ Mover -> shutil.move ou  os.rename
import os
import shutil


HOME = os.path.expanduser("~")
DESKTOPE = os.path.join(HOME, "Área de trabalho")
PASTA_ORIGINAL = os.path.join(DESKTOPE, "EXEMPLO")
NOVA_PASTA = os.path.join(DESKTOPE, "NOVA_PASTA")


shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.move(NOVA_PASTA, NOVA_PASTA + "_EITA")

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )

#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)
