import math # biblioteca matemática
metroquadrado = int(input("Digite quantos metros quadrados a ser pintados: "))
litros = metroquadrado/3
if litros<=18:
    print("Quantidade de lata a serem comprada é uma lata")
    print("O valor da conta a ser pago: R${:.2f}".format(80))
else:
   quantidadelatas = math.ceil(litros/18) # ceil para arredondar para cima / floor para arredondar para baixo
   precototal = quantidadelatas*80
   print("Quantidade de latas a serem compradas", quantidadelatas)
   print("O valor da conta a ser paga: R${:.2f}".format (precototal))
