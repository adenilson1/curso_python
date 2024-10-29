"""
Exercício - Lista de tarefas com desfazer e refazer
Musica para codar =)
Everybody wnats to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café] -> Adicionar fazer café
todo = ['fazer cafe','caminhar'] -> adicionar caminhar
desfazer = ['fazer cafe',] -> Refazer ['Caminhar]
desfazer = [] -> Refazer ['caminhar', 'fazer cafe]
refazer = todo ['fazer café']
refazer = todo ['fazer cadr], 'caminhar'
"""
import os
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa')
        print()
        return
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} foi removida da lista')
    tarefas_refazer.append(tarefa)
    print()

    
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        print()
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} foi adicionada da lista')
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)
    print(f'{tarefa=} foi adicionada da lista')
    print()





tarefas = []
tarefas_refazer = []
while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'clear':
        os.system('clear')
        continue

    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue