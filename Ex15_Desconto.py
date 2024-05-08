hora = float(input("Digite quanto você ganha por hora: "))
horatrabalhada = int(input("Digite quantas horas foram trabalhadas no mês: "))
salario = hora * horatrabalhada
impostorenda = (11/100*salario) # 11% descontado do salário bruto
inss = (8/100*salario) # 8% descontado do salário bruto
sindicato = (5/100*salario) # 5% descontado do salário bruto
salarioliquido = (salario - impostorenda - inss - sindicato)

print("Salário bruto:", salario)
print("Imposto de renda:", impostorenda)
print("INSS:", inss)
print("Sindicato:", sindicato)
print("Salário líquido:", salarioliquido)
