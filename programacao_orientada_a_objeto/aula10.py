# @staticmethod (metodos estaticos) são inúteis em PendingDeprecationWarning
# Métodos estáticos são métodos que estão denstro da 
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua 
# classe

class Classe:
    @staticmethod
    def funcao_que_esta_dentro_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)

#mesma coisa de uma funcao
def funcao(*args, **kwargs):
    print('Oi', args, kwargs)

c1 = Classe()
c1.funcao_que_esta_dentro_na_classe(1,2,3)
funcao(1,2,3)
Classe.funcao_que_esta_dentro_na_classe(nomeado=1)
funcao(nomeado=1)