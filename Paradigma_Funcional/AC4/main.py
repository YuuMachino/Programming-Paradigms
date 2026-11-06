from operacoes import (
    aplicar_desconto,
    calcular_faturamento,
    filtrar_aprovados,
    montar_dados_relatorio,
    pedidos_alto_valor,
    processar,
)
from relatorio import exibir_relatorio

PEDIDOS = [
    {"id": 1, "cliente": "Ana", "valor": 500, "status": "aprovado"},
    {"id": 2, "cliente": "Carlos", "valor": 150, "status": "pendente"},
    {"id": 3, "cliente": "Maria", "valor": 1200, "status": "aprovado"},
    {"id": 4, "cliente": "João", "valor": 80, "status": "aprovado"},
    {"id": 5, "cliente": "Fernanda", "valor": 300, "status": "cancelado"},
    {"id": 6, "cliente": "Pedro", "valor": 750, "status": "aprovado"},
]

PERCENTUAL_DESCONTO = 10
VALOR_MINIMO_ALTO = 500


def main():
    dados = montar_dados_relatorio(PEDIDOS, PERCENTUAL_DESCONTO, VALOR_MINIMO_ALTO)
    exibir_relatorio(dados)



if __name__ == "__main__":
    main()
