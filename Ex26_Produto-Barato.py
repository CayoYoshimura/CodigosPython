produto1 = float(input("Digite o preço do produto 1: "))
produto2 = float(input("Digite o preço do produto 2: "))
produto3 = float(input("Digite o preço do produto 3: "))

if (produto1 < produto2 and produto1 < produto3):
    print("O produto 1 é o produto mais barato")

elif (produto2 < produto1 and produto2 < produto3):
    print("O produto 2 é o produto mais barato")

elif (produto3 < produto1 and produto3 < produto2):
    print("O produto 3 é o produto mais barato")