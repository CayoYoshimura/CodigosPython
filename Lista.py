lista1 = ["oi"]
lista2 = [10, 20, 30]
print(lista1, lista2)

# Sublista

lista3 = ["oi", 2.0, 5, [10, 20]]
print(lista3)

# Contagem

lista4 = ["oi", 2.0, 5, [10, 20]]
print(len(lista4))

# Acesso a lista

numeros = [17, 123, 87, 34, 66, 8398, 44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])   # Conta da direita para esquerda sendo o 44 o número -1
print(numeros[-1])

# Contagem dentro de elementos
#            0   1     2                 3        4     5     6
#                    0123             01234567     
uma_lista = [3, 67, "gato", [56, 57, "cachorro"], [], 3.14, False]
print(uma_lista[3][2][1])   # Contagem da esquerda para direita começa com 0

# Pertinência em uma lista

frutas1 = ["maca", "laranja", "banana", "cereja"]
print("maca" in frutas1)   # True ou False
print("pera" in frutas1)   # True ou False
print("maca" not in frutas1) # True ou False

frutas2 = ["maca", "laranja", "banana", "cereja"]
print([1, 2] + [3, 4])   # junção de elementos
print(frutas2 + [6, 7, 8, 9]) # junção de elementos
print(["teste"] * 4)   # Multiplicação de elemento
print([1, 2, ["Ola", "adeus"]] * 2)   # Multiplicação de elemento