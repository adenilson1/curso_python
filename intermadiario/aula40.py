#Variaveis livres + nonlocal (local, global)

def fora(x):
    a = x # variavel livre, ou seja, nao definida na execução da funcao dentro
    
    def dentro():
        print(locals())
        print(dentro.__code__.co_freevars)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print()
print(dentro2())