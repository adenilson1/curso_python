# Relaçẽos entre classes: Associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligado dentro do sistema
# Essa é a relação mais comum entre objtos e tem subconjuntos
# como agregação e composição(que veremos depois)
# Geralmente, temos uma associação quando um objeto tem 
# um atributo que referencia outro objeto
# Associação não especifica como um objeto controla
# o ciclo de vida de outro objeto

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Adenilson')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_escrever = FerramentaDeEscrever('Maquina')
escritor.ferramenta = maquina_escrever
# escritor.ferramenta = caneta

print(caneta.escrever())
print(maquina_escrever.escrever())
print(escritor.ferramenta.escrever())