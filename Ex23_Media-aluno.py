nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2)/2

if (media == 10):
    print("Aprovado com Distinção!")
elif (media >= 7):
    print("Aprovado!")
else:
    print("Reprovado!")
   