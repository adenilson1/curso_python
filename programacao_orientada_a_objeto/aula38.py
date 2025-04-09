# Métodos especial __call__
# Callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma 
# classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone 

    def __call__(self, nome):
        print(nome, 'Tell', self.phone)
        return 1234

call1 = CallMe('123456789')
retorno = call1('Adenilson')
print(retorno)