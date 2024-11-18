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

class A:
    atributo_a = 'valor_a'

    def metodo(self):
        print('A')

class B(A):
    atributo_b= 'valor_b'

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor_c'

    def metodo(self):
        super().metodo()
        print('C')

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
