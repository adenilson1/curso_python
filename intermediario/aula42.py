def criar_funcao(func): # funcao decoradora
    def interna(*args, **kwargs):
        print('vou te decorar')

        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)
        resultado += ' QUALQUER COISA'
        print(f'o seu resultado foi {resultado}')
        print('ok, aogra voce foi decorada')

        return resultado
    return interna 



@criar_funcao #syntax sugar -> decorador
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('parametro deve ser uma string')

invertida = inverte_string('123')
print(invertida)