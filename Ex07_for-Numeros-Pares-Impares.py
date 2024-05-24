num = 1
par = impar = 0
while num != 0:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print("Você digitou {} números pares e {} números impares".format(par, impar))