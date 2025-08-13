# ZIP - COmpactando / Descompactando arquivos com zipfile.ZipFile

import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / "aula_28_diretorio_zip"
CAMINHO_COMPACTODO = CAMINHO_RAIZ / "aula_28_compactado.zip"
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / "aula28_descompactado"

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTODO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTODO).replace(".zip", ""), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Criar o diretorio para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_caminho(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = "arquivo_%s" % i
        with open(zip_dir / f"{texto}.txt", "w") as arquivo:
            arquivo.write(texto)


criar_caminho(10, CAMINHO_ZIP_DIR)
# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTODO, "w") as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTODO, "r") as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extrando arquivos de um zip
with ZipFile(CAMINHO_COMPACTODO, "r") as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
