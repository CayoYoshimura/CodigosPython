soma = 0
contador = 0
for conta in range(1, 7):
     num = int(input("Digite o {} valor: ".format(conta)))   # até aqui é o contador de for
     if num % 2 == 0:  # Apenas pegar os números pares
         soma += num 
         contador += 1
print(soma)
