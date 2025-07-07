# secrets gera números aleatórios seguros
import secrets

# import string as s
# from secrets import SystemRandom as Sr


# print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# Funções:
# seed
# -> NÃO FAZ NADA
# -> Inicializa o gerador de random (por isso "Números psedoaleatórios")
# random.seed(10)


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
nomes = ["Luiz", "Maria", "Helena", "Joana"]
# random.shuffle(nomes)
print(nomes)

# random.sample(iterável, k=N)
# -> Escolhe elementos do iterável e retorna outro iterável (não repete valroes)
novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choices(iterável, k=N)
# ->Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(novos_nomes)

# random.choice(Iterável)-> Escolhe um elemento do iterável
print(random.choice(nomes))
