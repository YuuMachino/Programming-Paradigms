from pedido import Pedido
from factories.comprovante_creator import ComprovanteCreator


class ProcessadorPedido:

    def __init__(self, pedido: Pedido, creator: ComprovanteCreator):
        self.__pedido = pedido
        self.__creator = creator

    def processar(self) -> str:
        total = self.__pedido.calcular_total_final()
        return self.__creator.emitir_comprovante(self.__pedido, total)
