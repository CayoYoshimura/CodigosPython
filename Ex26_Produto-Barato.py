produto1 = int(input("Digite um número 1: "))
produto2 = int(input("Digite um número 2: "))
produto3 = int(input("Digite um número 3: "))

if (produto1 > produto2 and produto1 > produto3):
    print("{} é maior que {} e {}".format(produto1, produto2, produto3))
    print("{} é menor que {} e {}".format(produto3, produto2, produto1))

elif (produto2 > produto1 and produto2 > produto3):
    print("{} é maior que {} e {}".format(produto2, produto1, produto3))
    print("{} é menor que {} e {}".format(produto1, produto3, produto2))

elif (produto3 > produto1 and produto3 > produto2):
    print("{} é maior que {} e {}".format(produto3, produto1, produto2))
    print("{} é menor que {} e {}".format(produto1, produto3, produto2))