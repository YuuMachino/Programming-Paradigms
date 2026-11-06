from abc import ABC, abstractmethod

class PedidoOberver(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        pass

class EmailObserver(PedidoOberver):
    def atualizar(self, mensagem):
        print(f"Email: {mensagem}")

class EstoqueObserver(PedidoOberver):
    def atualizar(self, mensagem):
        print(f"Estoque: {mensagem}")

class FinanceiroOberver (PedidoOberver):
    def atualizar (sef, mensagem):
        print(f"Fianceiro: {mensagem}")


class Pedido:
    def __init__(self):
        self.__observadores = []

    def adicionar_observer(self, observer: PedidoOberver):
        self.__observadores.append(observer)
    
    def remover_observer(self, observer= PedidoOberver):
        self.__observadores.remove(observer)
    
    def notificar(self, mensagem):
        for observer in self.__observadores:
            observer.atualizar(mensagem)

    def confirmar(self):
        print("Pedido confirmado")
        self.notificar("Novo pedido realizado")



pedido=Pedido()
pedido.adicionar_observer(EmailObserver())
pedido.adicionar_observer(EstoqueObserver())
pedido.adicionar_observer(FinanceiroOberver())

pedido.confirmar()