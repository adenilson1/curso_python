#Decoradores com paramentros

def decorada(func):
    print('Decorada 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada 


@decorada
def soma(x,y):
    return x + y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)