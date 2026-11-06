def calcular_desconto (valor, percentual):
    desconto = valor *percentual /100
    return valor - desconto

valor = float(input("Valor: "))
percentual = float(input("Desconto: "))
final = calcular_desconto(valor, percentual)
print("Valor final: ", final)