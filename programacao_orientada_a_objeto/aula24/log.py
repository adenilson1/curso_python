#Abstração
#Herança - é um 
class Log:
    def _log(self, msg): # assinatura do metodo
        raise NotImplementedError('Implemente o médoto log')


    def log_error(self, msg):
       return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
       return self._log(f'Success: {msg}')


class LogFileMexin(Log):
    def _log(self, msg):
        print(msg)



class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Qualquer coisa')
    l.log_success('Que Legal')
   

