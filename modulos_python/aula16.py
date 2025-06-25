# json. dump e json.load com arquivos

import json
import os

NOME_ARQUIVO = "aula16.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
)

# print(os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))

filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel ",
    "original_title": "The King of the Rings: THe Fellowship of thr Ring",
    "is_move": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Borom"],
    "budget": None,
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, "w") as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, "r") as arquivo:
    filme_do_json = json.load(arquivo)
print(filme_do_json)
