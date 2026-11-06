"""
Por que viola o SRP?
O Single Responsibility Principle diz: "uma classe deve ter apenas UM motivo para mudar"

Na classe original, Pedido fazia várias coisas:

Calculava o valor do pedido;
Salvava no banco de dados;
Enviava e-mail.

"""


class Pedido:
    TAXA = 0.10  

    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def calcular_total(self):
        return self.valor * (1 + self.TAXA)


class PedidoRepository:

    def salvar(self, pedido):
        print(f"Salvando pedido de {pedido.cliente} no banco de dados...")


class EmailService:

    def enviar_confirmacao(self, pedido):
        print(f"Enviando confirmação para {pedido.cliente}...")


def main():
    pedido = Pedido("Ana", 100)
    repositorio = PedidoRepository()
    email = EmailService()

    print(f"Total do pedido: R$ {pedido.calcular_total():.2f}")
    repositorio.salvar(pedido)
    email.enviar_confirmacao(pedido)


if __name__ == "__main__":
    main()
