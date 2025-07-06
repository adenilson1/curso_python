# random tem geradores de números psudoaletatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para sgurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo ,
# a saída pode ser previsível.

# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# Funções:
# seed
# -> Inicializa o gerador de random (por isso "Números psedoaleatórios")

# random.randrage (inicio, fim, passo)
# ->Gera um número inteiro aleatório dentro de um intervalo espercífico
r_range = random.randrange(10, 20, 2)
print(r_range)


# random.randint(inicio, fim)
# ->Gera um número aleatório dentre de um intervalo "sem passo"
r_range_int = random.randint(10, 20)
print(r_range_int)

# random.uniform(inicio, fim)
# -> Gera um número flutuante aleatório dentre de um intervalo "sem passo"
r_range_flut = random.uniform(10, 20)
print(r_range_flut)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
# random.choice(Iterável)-> Escolhe um elemento do iterável
# random.choices(iterável, k=N)
# ->Escolhe elementos do iterável e retorna outro iterável ()
