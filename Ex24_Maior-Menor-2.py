numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

if (numero1 > numero2 and numero1 > numero3):
    print("{} é maior que, {} e {}".format(numero1, numero2, numero3))

elif (numero2 > numero1 and numero2 > numero3):
    print("{} é maior que, {} e {}".format(numero2, numero1, numero3))

elif (numero3 > numero1 and numero3 > numero2):
    print("{} é maior que, {} e {}".format(numero3, numero1, numero2))