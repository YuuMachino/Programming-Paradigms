def exibir_relatorio(dados):
    print("===== RELATÓRIO DE VENDAS =====")
    print(f"Total de pedidos: {dados['total_pedidos']}")
    print(f"Pedidos aprovados: {dados['total_aprovados']}")
    print(f"Faturamento bruto: R$ {dados['faturamento_bruto']:.2f}")
    print(f"Faturamento com desconto: R$ {dados['faturamento_com_desconto']:.2f}")
    print("Pedidos de alto valor:")
    for pedido in dados["alto_valor"]:
        print(f"- {pedido['cliente']}: R$ {pedido['valor']:.2f}")
    print("Clientes com pedidos aprovados:")
    print(", ".join(dados["clientes_aprovados"]))
    print("================================")
