# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas, podemos seguir as seguintes convenções
# _ (sem underline) = public
# podem ser usado em qualquer lugar
# (um underline) = preotected
# não DEVE ser usado fora da classe ou suas subclasses
# __(dois underlines) = private
# "não mangling" (desfiguração de nomes ) em Python
# _NomeClasse__nome_attr_ou_method
# só devem ser usado na classe em que foi declarada.

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        # self._motedo_protected()
        # print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'isso é público'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    
    
f = Foo()
# print(f._protected)
# print(f.public)
print(f.metodo_publico())
print(f._Foo__metodo_private())