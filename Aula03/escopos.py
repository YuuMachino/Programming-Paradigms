#Escopo global, toa função ou processo pode acessa essa variavel
nome = "Carlos"

def mostrar_nome():
    #Escopo local, só aparece dentro dessa função
    nome="Maria"
    print(nome)
mostrar_nome()
print(nome)