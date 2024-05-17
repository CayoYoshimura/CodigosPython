lista = [[1, 2], [3], [4, 5, 6]]
soma = 0
for sublista in lista:
    somasublista = 0
    for num in sublista:
        somasublista += num
        print(somasublista)
    soma += somasublista

print(soma)