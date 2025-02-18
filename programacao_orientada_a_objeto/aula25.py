# Classe abastradas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem força outras classes
# a criarem médotos concretos. Também podem ter 
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com médotos 
# abstratos é que elas NÃO PODEM ser instânciadas 
# diretamente.
# Médotos abstratos DEVEM ser implementados 
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorato mais interno.

