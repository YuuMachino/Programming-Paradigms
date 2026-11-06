from factories.comprovante import Comprovante, formatar_moeda


class ComprovanteSimples(Comprovante):

    def emitir(self, pedido, total: float) -> str:
        return f"COMPROVANTE SIMPLES | Total pago: {formatar_moeda(total)}"


class ComprovanteDetalhado(Comprovante):

    def emitir(self, pedido, total: float) -> str:
        linhas = ["=== COMPROVANTE DETALHADO ==="]
        for produto in pedido.get_produtos():
            linhas.append(
                f"{produto.get_nome():<12} {produto.get_quantidade()} x "
                f"{formatar_moeda(produto.get_preco())} = "
                f"{formatar_moeda(produto.calcular_subtotal())}"
            )
        bruto = pedido.calcular_total_bruto()
        linhas.append("-" * 28)
        linhas.append(f"Total bruto:  {formatar_moeda(bruto)}")
        linhas.append(
            f"Desconto:     {pedido.get_desconto().get_nome()} (-{formatar_moeda(bruto - total)})"
        )
        linhas.append(f"Total final:  {formatar_moeda(total)}")
        return "\n".join(linhas)
