# Herança Múltipla - Python Orientado a Objetos
# QUer dizer que no Python, uma classe pode estender
# variais outras classes.
# Herança Simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> Filelog
# Animal ->Mamifero ->Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)

# Python3 usa C3 superclass linearization
# para gerar o mro 

# Para saber a ordem de chamada dos médotos
# Use o método de classes Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)
