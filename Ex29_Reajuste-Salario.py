salario = float(input("Digite o seu salário: "))

if (salario <= 280):
    aumento = 20/100*salario
    reajuste = salario+aumento

    print("Salario: R$ {:.2f}".format(salario))
    print("Percentual: 20%") 
    print("Valor do aumento: R$ {:.2f}".format(aumento))
    print("Novo salário: R$ {:.2f}".format(reajuste))

elif (salario > 280 and salario <= 700):
    aumento = 15/100*salario 
    reajuste = salario+aumento

    print("Salario: R$ {:.2f}".format(salario))
    print("Percentual: 15%")
    print("Valor do aumento: R$ {:.2f}".format(aumento))
    print("Novo salário: R$ {:.2f}".format(reajuste))

elif (salario > 700 and salario <= 1500):
    aumento = 10/100*salario
    reajuste = salario+aumento

    print("Salario: R$ {:.2f}".format(salario))
    print("Percentual: 10%")
    print("Valor do aumento: R$ {:.2f}".format(aumento))
    print("Novo salário: R$ {:.2f}".format(reajuste))

elif (salario > 1500):
    aumento = 5/100*salario
    reajuste = salario+aumento

    print("Salário: R$ {:.2f}".format(salario))
    print("Percentual: 5%")
    print("Valor do aumento: R$ {:.2f}".format(aumento))
    print("Novo salário R$ {:.2f}".format(reajuste))