from functools import reduce


def filtrar_aprovados(pedidos):
    return list(filter(lambda pedido: pedido["status"] == "aprovado", pedidos))


def aplicar_desconto(pedidos, percentual):
    fator = 1 - percentual / 100
    return list(map(lambda pedido: {**pedido, "valor": pedido["valor"] * fator}, pedidos))


def calcular_faturamento(pedidos):
    return reduce(lambda total, pedido: total + pedido["valor"], pedidos, 0)


def pedidos_alto_valor(pedidos, valor_minimo):
    return list(filter(lambda pedido: pedido["valor"] > valor_minimo, pedidos))


def nomes_clientes(pedidos):
    return list(map(lambda pedido: pedido["cliente"], pedidos))


def processar(pedidos, operacao):
    return operacao(pedidos)


def montar_dados_relatorio(pedidos, percentual_desconto, valor_minimo):
    aprovados = processar(pedidos, filtrar_aprovados)
    return {
        "total_pedidos": len(pedidos),
        "total_aprovados": len(aprovados),
        "faturamento_bruto": processar(aprovados, calcular_faturamento),
        "faturamento_com_desconto": processar(
            aprovados,
            lambda lista: calcular_faturamento(aplicar_desconto(lista, percentual_desconto)),
        ),
        "alto_valor": processar(
            aprovados,
            lambda lista: pedidos_alto_valor(lista, valor_minimo),
        ),
        "clientes_aprovados": processar(aprovados, nomes_clientes),
    }
