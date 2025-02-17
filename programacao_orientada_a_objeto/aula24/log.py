#Abstração
#Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.text'

class Log:
    def _log(self, msg): # assinatura do metodo
        raise NotImplementedError('Implemente o médoto log')


    def log_error(self, msg):
       return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
       return self._log(f'Success: {msg}')


class LogFileMexin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando...')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')




class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que Legal')

    lf = LogFileMexin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que Legal')
 
   

