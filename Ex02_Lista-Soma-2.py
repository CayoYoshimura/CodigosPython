lista = [[1, 2, 3]]
soma = 0
for sublista in lista:
    somasublista = 0
    for num in sublista:
        somasublista += num
        print(somasublista)
    soma += somasublista