# @property - um getter no modo Pythonico
# getter - um médoto para obeter um atributo 
# cor -> get cor()
# modo puthonico - modo python de fazer coisas 
# @property é uma propriedade do objeto, ela 
# é um método que se comporta como um atributo 
# Geralemte é usada nas seguntes situações:
# - como getter 
# - p/ evitar quebrar código cliente
# - p/ habilitar setter 
# - p/ executar ações ao obter um atributo 
# codigo cliente é o codigo que usa o seu codigo

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta= cor
    
#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta 

# ################################

# caneta = Caneta('Azul')     
# print(caneta.get_cor()) 
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor()) 



class Caneta:
    def __init__(self, cor):
        self.cor_tinta= cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return '12345'

################################

caneta = Caneta('Azul')     
print(caneta.cor) 
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)