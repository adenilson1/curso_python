"""
Este é um módulo de exemplo

Este módulo cotém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""

variavel_1 = 1


class Foo:
    def soma(self,x: int | float, y: int | float) -> int | float:
     
     """
        Este é um módulo de exemplo

        Este módulo cotém funções e exemplos de documentação de funções.
        A função soma você já conhece bastante.
    """
    
     """ 
        Soma x e y

        :param x: Número 1
        :type y: int or float
        :param y: Número 2
        :type y: int or float
        :return: A soma entre x e y
        :type: int or float
        """
     return x + y


    def multiplica(
            self,
            x: int | float,
            y: int | float,
            z: int | float | None = None
    ) -> int | float:
        """
        Multiplição x,y e/ou z

        Multiplicação x e y. Se z enviado, mulplica x, y, z.
        """
        if z is None:
            return x * y
        return x * y * z
    
    def bar(self) -> int:
       """
       O que ele faz

       :raises NotImplementedError: Se o método não for definido
       :raises ValueError: Se o método não for definido
       """
       raise NotImplementedError('TESTE')

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4