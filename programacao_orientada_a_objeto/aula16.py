# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu cilco de vida independente.
# Geralmente é uma relação de um para muitos, onde um 
# objeto tem um ou muitos objetos.
# Os objetos podem viver separamdamente, mas pode
# se tratar de uma relação onde um objeto precisa de 
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        #self._produtos.extend(produtos)
        #self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    
    def lista_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho() 
p1, p2 = Produto('Caneta', 1.20), Produto('Camisa',20) 
carrinho.inserir_produtos(p1,p2)
carrinho.lista_produtos()
print(carrinho.total())
