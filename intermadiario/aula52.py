"""
Funções recursivsa e recursividade
-funções que podem se chamar de volta
- uteis para dividir prblemas grandes em partes menores
Toda função recursiva deve ser:
-Um problema que possa ser dividida em partes menores
-Um caso recursivo que resolve o pequeno problema 
-Um caso base que para a recursão 
-fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
"""
"""
import sys
sys.setrecursionlimit(1004)

def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    #caso de segurança: base
    if inicio >= fim:
        return fim

    #caso recursivo
    #contar ate o chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(0,1000))
"""
def factorial(n):
    if n <= 1:
        return 1
    return n *  factorial(n-1)

print(factorial(5))
print(factorial(10))
#print(factorial(100) quebra o codigo, maior que 1000