#Variaveis livres + nonlocal (local, global)

def fora(x):
    a = x # variavel livre, ou seja, nao definida na execução da funcao dentro
    
    def dentro():
        print(locals())
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print()
print(dentro2())

print(50*'-')
print()

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # fora da função, o python busca em outro local
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)