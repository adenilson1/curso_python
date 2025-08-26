# argparse. ArgumentParser para argumentos mais complexos
# Tutorial Oficial: 
# https://docs.python.org/3/howto/argparse.html 

from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('-b', '--basic',
                    help="Mostra 'Ola Mundo' na tela",
                    # type=str,
                    metavar='STRING',
                    # default='Olá Mundo',
                    required=False,
                    # nargs='+', # recebe mais de um valor
                    action='append', #recebe o argumento mais de uma vez
                    )
args = parser.parse_args()
# print(args.b)

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.baseic)
else:
    print('O valor de basic ',args.basic)