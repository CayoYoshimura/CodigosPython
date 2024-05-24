s = 0
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")
    
if pergunta1 == 's':
    s += 1

if pergunta2 == 's':
    s += 1

if pergunta3 == 's':
    s += 1

if pergunta4 == 's':
    s += 1

if pergunta5 == 's':
    s += 1

if s == 2:
    print("Suspeita!")
elif s == 3 or s == 4:
    print("Cúmplice!")
elif s == 5:
    print("Assassino!")
else:
    print("Inocente!")