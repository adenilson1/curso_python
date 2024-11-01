# Matendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando ...')
            return

        print(f'{self.nome} está filmando ...')
        self.filmando = True


    def fotografrar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        print(f'{self.nome} está fotografando ...')
        self.foto = True


    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando ...')
            return
        
        print(f'{self.nome} está parando de filmar ...')
        self.filmando = False

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografrar()
c1.parar_de_filmar()
c1.fotografrar()
print()
c2.filmar()
c2.filmar()
c2.fotografrar()
c2.parar_de_filmar()
c2.fotografrar()