from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        ...


class Pix(Pagamento):
    def processar(self, valor):
        print(f"PIX de R$ {valor}")


class Cartao(Pagamento):
    def processar(self, valor):
        print(f"Cartão de R$ {valor}")


class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Boleto de R$ {valor}")


class PagamentoRepository:
    def salvar(self, pagamento, valor):
        print(f"Salvando pagamento ({type(pagamento).__name__}, R$ {valor}) no banco...")


class ComprovanteService:
    def enviar(self, pagamento, valor):
        print(f"Enviando comprovante de R$ {valor} por e-mail...")

class Criptomoeda(Pagamento):
    def processar(self, valor):
        print(f"Criptomoeda de R$ {valor}")


def main():
    pagamentos = [
        Pix(),
        Cartao(),
        Boleto(),
        Criptomoeda(),  
    ]

    repositorio = PagamentoRepository()
    comprovante = ComprovanteService()

    for pagamento in pagamentos:
        pagamento.processar(500)
        repositorio.salvar(pagamento, 500)
        comprovante.enviar(pagamento, 500)
        print()


if __name__ == "__main__":
    main()
