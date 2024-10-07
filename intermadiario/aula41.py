def criar_funcao(func): # funcao decoradora
    def interna(*args, **kwargs):
        print('vou te decorar')

        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)
        print(f'o seu resultado foi {resultado}')
        print('ok, aogra voce foi decorada')

        return resultado
    return interna 




def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('parametro deve ser uma string')

inverte_string_checando_paramatro = criar_funcao(inverte_string)
invertida = inverte_string_checando_paramatro('123')
print(invertida)