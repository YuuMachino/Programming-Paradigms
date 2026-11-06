# Sistema de Processamento de Vendas

Sistema em Python, executado pelo terminal, que analisa pedidos usando programação funcional (`map`, `filter`, `reduce`, funções puras, funções de alta ordem e `lambda`).

## Requisitos

- Python 3.8 ou superior (nenhuma biblioteca externa)

## Como executar

Dentro da pasta `sistema_vendas`, rode:

```
python main.py
```

## Estrutura

- `main.py`: dados iniciais e execução.
- `operacoes.py`: funções puras de filtragem, desconto, cálculo e montagem dos dados do relatório.
- `relatorio.py`: apresentação dos resultados no terminal.
- `README.md`: instruções de uso.

## Funções principais (`operacoes.py`)

- `filtrar_aprovados(pedidos)`: usa `filter()` para manter apenas pedidos aprovados.
- `aplicar_desconto(pedidos, percentual)`: usa `map()` e devolve novos dicionários, sem alterar os originais.
- `calcular_faturamento(pedidos)`: usa `reduce()` para somar os valores.
- `pedidos_alto_valor(pedidos, valor_minimo)`: seleciona pedidos com valor estritamente maior que o limite.
- `processar(pedidos, operacao)`: função de alta ordem que executa a operação recebida.
- `montar_dados_relatorio(...)`: reúne todos os cálculos em um dicionário, separado da apresentação.

## Saída esperada

```
===== RELATÓRIO DE VENDAS =====
Total de pedidos: 6
Pedidos aprovados: 4
Faturamento bruto: R$ 2530.00
Faturamento com desconto: R$ 2277.00
Pedidos de alto valor:
- Maria: R$ 1200.00
- Pedro: R$ 750.00
Clientes com pedidos aprovados:
Ana, Maria, João, Pedro
================================
```
