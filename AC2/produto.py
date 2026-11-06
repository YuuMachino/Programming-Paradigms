class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def entregar(self):
        pass

class Fornecedor:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, nomeFornecedor):
        super().__init__(nome, preco)
        self.fornecedor = Fornecedor(nomeFornecedor)

    def entregar(self):
        super().entregar()
        print(f"O produto físico será enviado pelos Correios pelo fornecedor: {self.fornecedor.get_nome()}")

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, nomeFornecedor):
        super().__init__(nome, preco)
        self.fornecedor = Fornecedor(nomeFornecedor)

    def entregar(self):
        super().entregar()
        print(f"O produto digital será enviado por download pelo fornecedor: {self.fornecedor.get_nome()}")

produtos = [
    ProdutoFisico("controle", "19,99", "samsung"),
    ProdutoDigital("joguinho", "20,50", "JogosINC")
]
for produto in produtos:
    produto.entregar()