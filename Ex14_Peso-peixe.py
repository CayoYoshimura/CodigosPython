peso = float(input("Digite o peso do peixe: "))

if (peso>50):
    limite = peso-50
    multa = limite*4
    print("O valor da multa: R${:.2f}".format(multa))