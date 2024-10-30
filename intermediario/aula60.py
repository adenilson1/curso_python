#evitando uso de condicionais - guard clause

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
    listar(tarefas)

    
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
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)
    print(f'{tarefa=} foi adicionada da lista')
    print()
    listar(tarefas)

tarefas = []
tarefas_refazer = []
while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comdados = {
        'listar': lambda:listar(tarefas),
        'desfazer':lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda:refazer(tarefas, tarefas_refazer),
        'clear': lambda:os.system('clear'),
        'adicionar': lambda:adicionar(tarefa, tarefas),
    }

    comdado = comdados.get(tarefa) if comdados.get(tarefa) is not None else \
         comdados['adicionar']
    comdado()


    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue

    # elif tarefa == 'clear':
    #     os.system('clear')
    #     continue

    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue

