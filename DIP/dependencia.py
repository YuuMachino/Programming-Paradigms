#quando uma classe é dependende de outra classe, e quando tentamos
#modificar, teremos dificuldades
"""
isso é um exemplo de dependencia errada
class Emailenviar:
    def enviar(self,mensagem):
        print("Email: ", mensagem)

class PedidoService:
    def finalizar(self):
        email=Emailenviar()
        print("Pedido finalizado")
        email.enviar("Seu pedido foi finalizado")

"""

from abc import ABC, abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem)
    pass

class EmailNotificador(Notificador):
    def enviar(self, mensagem)
        print("Email: ", mensagem)

class SMSNotificador(Notificador):
    def enviar(self, mensagem)
        print("SMS: ", mensagem)


class PedidoService:
    def __init__(self, notificador: Notificador ):
        self.notificador = notificador

    def finalizar(self):
        print("Pedido finalizado")
        self.notificador.enviar("Seu pedido foi finalizado")


email: EmailNotificador()
sms: SMSNotificador()

pedido = PedidoService(sms)

pedido.finalizar

"""
O que tudo isso faz? 
basicamente, a classe notificador tem apenas uma classe onde ambas as classes de email e sms
sao dependentes, porem outras classes não não, então, quando trabalhamos com o pedidoservicde
nao somos dependentes apenas do email ou do sms, temos o poder de escolher o que queremos
tudo pelo notificador que encaminhará para a classe certa
"""