hora = float(input("Digite quanto que você ganha por hora: "))
horatrabalhadas = int(input("Digite quantas hora foram trabalhadas no mês: "))

salario = hora * horatrabalhadas
print("Seu salário: R${:.2f}".format(salario))