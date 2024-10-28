
import copy
from dados import produtos
#Exercicios
#1) Aumente o proço dos produtos em 10%
#2) Gere novos produtos po deep copy (copia profunda)
novos_produtos =[
    
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)

]

#3) Ordene od produtos po nome decrescente 
#4) Gere produto ordenados por nome por deep copy

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['nome'],
    reverse=True
)

#5) Ordene os produtos por preço crescente
#6) Gere produto ordenados por preço por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['preco']
)


#FINAL
print('Produtos')
print(*produtos, sep='\n')
print()
print('Novos produtos com 10% de aumento')
print(*novos_produtos, sep='\n')
print()
print('Produtos ordenados por nome decrescente')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('Produtos ordenados por preço crescente')
print(*produtos_ordenados_por_preco, sep='\n')