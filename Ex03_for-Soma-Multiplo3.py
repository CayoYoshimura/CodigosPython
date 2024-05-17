soma = 0
contador = 0
for cont3 in range(1, 10, 2):
   if cont3 % 3 == 0:
      soma += cont3
      contador += 1
print("Resultado da soma: {}".format(soma))
print("Resultado de números impares: {}".format(contador))
