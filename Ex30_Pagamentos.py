hora = int(input("Digite quanto você ganha por hora: "))
horatrabalhada = int(input("Digite quantas horas foram trabalhadas: "))
salario = hora * horatrabalhada

if (salario <= 900):
    inss = 10/100 * salario
    fgts = 11/100 * salario
    descontos = inss
    salarioliquido = salario - descontos
    print("Salário Bruto: ({} * {})   :R$ {:.2f}".format(hora, horatrabalhada, salario))
    print("(-) INSS (10%)   :R$ {:.2f}".format(inss))
    print("FGTS (11%)   :R$ {:.2f}".format(fgts))
    print("Total de descontos   :R$ {:.2f}".format(descontos))
    print("Salário Líquido   :R$ {:.2f}".format(salarioliquido))

elif (salario <= 1500):
    impostorenda = 5/100 * salario
    inss = 10/100 * salario
    fgts = 11/100 * salario
    descontos = inss + impostorenda
    salarioliquido = salario - descontos
    print("Salário Bruto: ({} * {})   :R$ {:.2f}".format(hora, horatrabalhada, salario))
    print("(-) IR (5%)   :R$ {:.2f}".format(impostorenda))
    print("(-) INSS (10%)   :R$ {:.2f}".format(inss))
    print("FGTS (11$)   :R$ {:.2f}".format(fgts))
    print("Total de descontos   :R$ {:.2f}".format(descontos))
    print("Salário Líquido   :R$ {:.2f}".format(salarioliquido))

elif (salario <= 2500):
    impostorenda = 10/100 * salario
    inss = 10/100 * salario
    fgts = 11/100 * salario
    descontos = inss + impostorenda
    salarioliquido = salario - descontos
    print("Salário Bruto: ({} * {})   :R$ {:.2f}".format(hora, horatrabalhada, salario))
    print("(-) IR (10%)   :R$ {:.2f}".format(impostorenda))
    print("(-) INSS (10%)   :R$ {:.2f}".format(inss))
    print("FGTS (11%)   :R$ {:.2f}".format(fgts))
    print("Total de descontos   :R$ {:.2f}".format(descontos))
    print("Salário Líquido   :R$ {:.2f}".format(salarioliquido))

elif (salario > 2500):
    impostorenda = 20/100 * salario
    inss = 10/100 * salario
    fgts = 11/100 * salario
    descontos = inss + impostorenda
    salarioliquido = salario - descontos
    print("Salário Bruto: ({} * {})   :R$ {:.2f}".format(hora, horatrabalhada, salario))
    print("(-) IR (20%)   :R$ {:.2f}".format(impostorenda))
    print("(-) INSS (10%)   :R$ {:.2f}".format(inss))
    print("FGTS (11%)   :R$ {:.2f}".format(fgts))
    print("Total de descontos   :R$ {:.2f}".format(descontos))
    print("Salário Líquido   :R$ {:.2f}".format(salarioliquido))