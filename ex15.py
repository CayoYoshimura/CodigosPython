h = float(input("Digite quanto você ganha por hora: "))
ht = int(input("Digite quantas horas foram trabalhadas no mês: "))
sal = h * ht
ir = (11/100*sal)
inss = (8/100*sal)
sin = (5/100*sal)
sl = (sal - ir - inss - sin)

print("Salário bruto:", sal)
print("Imposto de renda:", ir)
print("INSS:", inss)
print("Sindicato:", sin)
print("Salário líquido:", sl)