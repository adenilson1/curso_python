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
def recursiva(inicio=0, fim=4):
    #caso de segurança: base
    print(inicio, fim)
    if inicio >= fim:
        return fim
    
  


    #caso recursivo
    #contar ate o chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())