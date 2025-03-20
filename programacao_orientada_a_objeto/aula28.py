# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que 
# classes derivadas de uma mesma superclasse
# tenham médotos iguais (com mesma assinatura)
# mas comprtamentos diferentes.
# Assinatura do médoto = Mesmo nome e quantidade
# de paâmentros (retorno não faz parte da assintura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID 
# Príncipio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis 
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)
# Sobreposição de métodos (override)

from abc import ABC, abstractmethod

class Notificacao:
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoeMail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviado - ' , self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('E-SMS: enviado - ' , self.mensagem)
        return True


# n = NotificacaoeMail('TESTANDO NOTIFICAÇÃO')
# n.enviar()

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoeMail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)

