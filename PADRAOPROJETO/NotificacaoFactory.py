
from abc import ABC, abstractmethod


# Produto abstrato
class NotificacaoFactory(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass
    
    @abstractmethod
    def salvar(self):
        pass

# Produtos concretos
class Email(NotificacaoFactory):
    def enviar(self, mensagem):
        print(f"Email enviado: {mensagem}")
    def salvar(self):
        print("Salvando email no banco de dados")


class SMS(NotificacaoFactory):
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")
    def salvar(self):
        print("Salvando SMS no banco de dados")


# Criador abstrato
class NotificacaoCreator(ABC):
    @abstractmethod
    def criar_notificacao(self) -> NotificacaoFactory:
        pass

    def notificar(self, mensagem):
        notificacao = self.criar_notificacao()
        notificacao.enviar(mensagem)
        notificacao.salvar()
        print("Processo executado")


# Criadores concretos
class EmailCreator(NotificacaoCreator):
    def criar_notificacao(self) -> NotificacaoFactory:
        return Email()


class SMSCreator(NotificacaoCreator):
    def criar_notificacao(self) -> NotificacaoFactory:
        return SMS()


# Execução
email = EmailCreator()
sms = SMSCreator()

email.notificar("Pedido aprovado")
sms.notificar("Pagamento aprovado")
