# Context Manager com classes
# Implementação de protocolos e dunder methods
# Processo chamado de Duck tiping, conceito relacionado
# com tipagem dinâmica onde o Pyhton não está interessado no tipo
# , mas se alguns métodos existem no objeto para que 
# funcione de forma adequada.

# Ex:
# with open('aula33.txt','w') as arquivo:
#     ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
         self.caminho_arquivo = caminho_arquivo
         self.modo = modo
         self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()


#instancia = MyContextManager('aula33.txt','w')

with MyOpen('aula33.txt','w') as arquivo:
        arquivo.write('Linha 1\n')
        arquivo.write('Linha 2\n')
        arquivo.write('Linha 3\n')
        print('WITH', arquivo)

    