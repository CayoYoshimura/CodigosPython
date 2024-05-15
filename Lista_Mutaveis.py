frutas1 = ["banana", "maca", "cereja"]

frutas1[0] = "pera"
frutas1[-1] = "Laranja"
print(frutas1)

# Simplicado

frutas2 = ['a', 'b', 'c', 'd', 'e', 'f']
frutas2[1:3] = ['x', 'y']
print(frutas2)

# Adição de elementos

lista = ['a', 'd', 'f']
lista[1:1] = ['b', 'c']
print(lista)

lista[4:4] = ['e']
print(lista)

lista[4:] = ['g']    # Substituição
print(lista)

# Remoção de elementos

a = ['um', 'dois', 'tres']
del a[1]
print(a)

lista2 = ['a', 'b', 'c', 'd', 'e', 'f']
del lista2[1:5]
print(lista2)

# Outra forma de remoção

g = [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9]
g.pop()
print(g)

g.pop(0)
print(g)

# append

b = [81, 82, 83]
b.append(5)   # Adiciona no final
print(b)

# extend

lista3 = [1,2]
lista3.extend([3,4])   # Adiciona mais de um no final
print(lista3)

# Ordenação ( sort )

c = [3, 2, 5, 6]
c.sort()      # Ordem crecente
print(c)
c.sort(reverse=True)     # Ordem decrecente
print(c)

# index

d = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]
print (d.index(4))    # Qual é a posição

# insert

e = [1, 2, 3, 4]
e.insert(1,100)   # Adiciona na posição desejada
print(e)

# Repetição

f = [88, 81, 82, 83, 88, 85, 88, 86]
print(f)
print(f.count(88))  # Quantas vezes apareceu determinado elemento