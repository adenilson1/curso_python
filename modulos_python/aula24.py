# Variáveis de ambiente Python
# Para variávies de ambiente
# Windows PS: $env:VARIAVEL = "VALOR" | echo $VARIAVEL
# Linux e Mac: export NOME_VARIAVEL = "VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variável de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load-dotenv
# load_dotenv()
# OBS: sempre lembre-se de criar um .env-exemple

import os

print(os.getenv("SENHA"))
