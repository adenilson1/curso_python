#Abstração
class Log:
    def log(self, msg): # assinatura do metodo
        raise NotImplementedError('Implemente o médoto log')


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)


if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Qualquer coisa')
   
