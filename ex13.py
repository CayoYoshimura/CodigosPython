h = float(input("Digite a altura: "))
sexo = input(("Digite qual é o seu gênero: "))

if (sexo=='m'):
    ideal = (72.7*h) - 58
    print("Seu peso ideal:", ideal)

elif (sexo=='f'):
    ideal = (62.1*h) - 44.7
    print("Seu peso ideal:", ideal)