mbps = float(input("Digite a velocidade em Mbps: "))
mb = float(input("Digite o tamanho do arquivo em MB: "))
tempo = (mb/mbps)/60
print("%.1f"%tempo)