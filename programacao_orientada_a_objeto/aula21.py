# super() é super classe na sub classe 
# Classe principal (Pessoa)
#  -> super class, base class, parent class
# Classe filhas (Cliente)
#  -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU A UPPER')
#         retorno =  super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    atributo_a = 'valor_a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b= 'valor_b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor_c'

    def __init__(self, *args, **kwargs):
        # print('BURLEI O SISTEMA')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super().metodo() #B
        # super(B, self).metodo() #A
        # super(A ,self).metodo()  #objetct

        A.metodo(self)
        B.metodo(self)
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())


c = C('atributo','qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()