# __new__ e __init__ em classes Python

class A:

    def __new__(cls,*args,**kwargs): # criar a instancia
        print('Antes de criar a instancia')
        instancia = super().__new__(cls)
        print('Depois de criar a instancia')
        instancia.x = 123
        return instancia
        
    def __init__(self, x):
        self.x = x
        print('Sou o init')
    
    def __repr__(self):
        return 'A()'

a = A(321)
print(a.x)

