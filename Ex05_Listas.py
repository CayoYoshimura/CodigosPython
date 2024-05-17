listas = [0, 1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
print(listas[1:9])
print(listas[8:10])
listapar = []
listaimpar = []

for x in listas:
    if x % 2 == 0:
        listapar.append(x)
    elif x % 2 == 1:
        listaimpar.append(x)

print(listapar)
print(listaimpar)
listas.sort(reverse=True)
print(listas)