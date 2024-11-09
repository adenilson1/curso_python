# @property - um getter no modo Pythonico
# getter - um médoto para obeter um atributo 
# modo puthonico - modo python de fazer coisas 
# @property é uma propriedade do objeto, ela 
# é um método que se comporta como um atributo 
# Geralemte é usada nas seguntes situações:
# - como getter 
# - p/ evitar quebrar código cliente
# - p/ habilitar setter 
# - p/ executar ações ao obter um atributo 

class Caneta:
    def __init__(self, car):
        self.car= car
        