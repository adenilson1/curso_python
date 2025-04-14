# __call__ de uma metacla

def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type): # cria a classe Pessoa
    def __new__(mcs, nome, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, nome, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')
        return cls      
    
    def __call__(cls, *args, **kwargs):
     
     instancia = super().__call__(*args, **kwargs)

     if 'nome' not in instancia.__dict__ :
        raise NotImplementedError('Crie o attr nome')
     
     return instancia

class Pessoa(metaclass = Meta): # contruindo a instancia
    #falar = 1234
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome): # atribuidos da instancia 
        print('MEU INIT')
        #self.nome = nome
    
    def falar(self):
         print('FALANDO...')



p1 = Pessoa('Adenilson')
p1.falar()
#print(p1.attr)
#print(p1)