n1=int(input("Informe a primeira nota: "))
n2=int(input("Informe a segunda nota: "))
n3=int(input("Informe a terceira nota: "))

#media=(n1+n2+n3)/3

#if media >=6:
    #print("Aluno aprovado")
#else:
    #print("Aluno reprovado")

#transforme o algoritmo em uma função

def media(a,b,c):
    m=(a+b+c)/3
    if m >=6:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

media(n1,n2,n3)