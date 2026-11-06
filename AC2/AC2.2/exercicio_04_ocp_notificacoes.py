from abc import ABC, abstractmethod


class Notificador(ABC):

    @abstractmethod
    def enviar(self, mensagem):
        ...

class Email(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando EMAIL: {mensagem}")


class SMS(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")


class WhatsApp(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando WhatsApp: {mensagem}")


def enviar_notificacao(notificador, mensagem):
    notificador.enviar(mensagem)

class PushNotification(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando PUSH: {mensagem}")


def main():
    email = Email()
    sms = SMS()
    enviar_notificacao(email, "Pedido realizado!")
    enviar_notificacao(sms, "Pagamento aprovado!")

    enviar_notificacao(WhatsApp(), "Seu pedido saiu para entrega!")
    enviar_notificacao(PushNotification(), "Você tem uma nova oferta!")


if __name__ == "__main__":
    main()
