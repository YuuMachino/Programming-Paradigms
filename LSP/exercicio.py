class Pagamento:
    def pagar(self, valor):
        print(f"Pagamento de R$ {valor} realizado")

class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pix de {valor} realizado")

class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Cartão de {valor} realizado")


class Boleto(Pagamento):
    def pagar(self, valor):
        raise Exception ("Não suportado")

def finalizar_pagamento(pagamento, valor):
    pagamento.pagar(valor)

pix=Pix()
cartao=Cartao()
boleto=Boleto()

finalizar_pagamento(pix, 200)
finalizar_pagamento(cartao, 200)
finalizar_pagamento(boleto, 200)

"""
Se a classe pai e a classe filha tiverem metodos diferentes, eles quebram a regra liscov,
ela funciona onde, se a boleto substituir a classe pagamento, o codigo ainda funcionaria sem problemas 
pois a principio, elas fazem a mesma coisa
"""