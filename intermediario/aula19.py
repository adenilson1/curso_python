"""
Exemplo de uso do tipo set
"""

letras = set()
while True:
    letra = input ('Digite uma letra: ')
    letras.add(letra.lower())
    print(letras)

    if 'l' in letras:
        print('PARABÉNS')
        break