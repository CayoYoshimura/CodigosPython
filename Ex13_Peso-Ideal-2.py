altura = float(input("Digite a altura: "))
sexo = input(("Digite qual é o seu gênero: "))

if (sexo=='m'): # 'm' para masculino
    ideal = (72.7*altura) - 58
    print("Seu peso ideal:", ideal)

elif (sexo=='f'): # 'f' para feminino
    ideal = (62.1*altura) - 44.7
    print("Seu peso ideal:", ideal)
