numero1 = int(input("Digite um número 1: "))
numero2 = int(input("Digite um número 2: "))
numero3 = int(input("Digite um número 3: "))

if (numero1 > numero2 and numero1 > numero3):
    print("{} é maior que {} e {}".format(numero1, numero2, numero3))
    print("{} é menor que {} e {}".format(numero3, numero2, numero1))

elif (numero2 > numero1 and numero2 > numero3):
    print("{} é maior que {} e {}".format(numero2, numero1, numero3))
    print("{} é menor que {} e {}".format(numero1, numero3, numero2))

elif (numero3 > numero1 and numero3 > numero2):
    print("{} é maior que {} e {}".format(numero3, numero1, numero2))
    print("{} é menor que {} e {}".format(numero1, numero3, numero2))