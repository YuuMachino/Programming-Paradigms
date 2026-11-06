from produto import Produto
from pedido import Pedido
from processador import ProcessadorPedido
from strategies.desconto import DescontoStrategy
from strategies.descontos_concretos import DescontoComum, DescontoVIP, DescontoPremium
from factories.comprovante_creator import (
    ComprovanteSimplesCreator,
    ComprovanteDetalhadoCreator,
)


class DescontoEspecial(DescontoStrategy):

    def calcular(self, valor: float) -> float:
        return valor - (valor * 0.15)


def montar_pedido(desconto: DescontoStrategy) -> Pedido:
    pedido = Pedido(desconto)
    pedido.adicionar_produto(Produto("Notebook", 3500.00, 1))
    pedido.adicionar_produto(Produto("Mouse", 80.50, 2))
    pedido.adicionar_produto(Produto("Teclado", 150.00, 1))
    return pedido


def main() -> None:
    descontos = [
        DescontoComum(),
        DescontoVIP(),
        DescontoPremium(),
        DescontoEspecial(),
    ]
    creators = [ComprovanteSimplesCreator(), ComprovanteDetalhadoCreator()]

    for desconto in descontos:
        print(f"\n##### {desconto.get_nome()} #####")
        for creator in creators:
            pedido = montar_pedido(desconto)
            processador = ProcessadorPedido(pedido, creator)
            print(processador.processar())
            print()

    print("##### Validações #####")
    for nome, preco, qtd in [("Inválido", -10, 1), ("Inválido", 10, 0)]:
        try:
            Produto(nome, preco, qtd)
        except ValueError as erro:
            print(f"Erro esperado: {erro}")


if __name__ == "__main__":
    main()
