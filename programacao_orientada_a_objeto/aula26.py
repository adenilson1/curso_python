# abstractmethod para qualquer método já decorado
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso 
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palabras usadas como pleceholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self,nome):
        self._name = None
        self.name = nome
 

    @property
 #   @abstractmethod
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self):...

 

class Foo(AbstractFoo):
    #name = ''

    def __init__(self, name):
        super().__init__(name)
#        print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self,name):
    #     self._name = name

foo = Foo('Bar')
print(foo.name)
oi