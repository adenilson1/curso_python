# lista de tarefas em json

import json
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

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print('Arquivo não existir')
        salvar(tarefas, caminho_arquivo)

    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo,'w',encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula61.json'
tarefas = ler([], CAMINHO_ARQUIVO)
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
    salvar(tarefas, CAMINHO_ARQUIVO)