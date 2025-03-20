# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar alguma exceção da linguagem.
# Arecomendação da doc é herdar de Exception.
# https://docs.python.org
# Criando exceções (comum colocar Error ao final)
# Levantado (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionado notas em exceções.

class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
        exception_ = MeuError('a','b','c')
        raise exception_

try:
      levantar()
except (MeuError, ZeroDivisionError) as error:
      print(error.__class__.__name__)
      print(error.args)
      print()
      exception_ = OutroError('Vou lançar de novo')
      raise exception_ from error 