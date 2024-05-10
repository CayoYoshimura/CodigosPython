import math
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada:"))
area_a_ser_pintada_com_folga = area_a_ser_pintada * 1.1
litros_de_tinta = area_a_ser_pintada_com_folga / 6
quantidade_latas_18 = math.ceil(litros_de_tinta / 18)
quantidade_latas_36 = math.ceil(litros_de_tinta / 3.6)
preco_latas_18 = quantidade_latas_18 * 80.00
preco_galoes_36 = quantidade_latas_36 * 25.00

quantidade_latas_mix = quantidade_latas_18
quantidade_galoes_mix = math.ceil((litros_de_tinta - quantidade_latas_18 * 18) / 3.6)
preco_mix = quantidade_latas_mix * 80.00 + quantidade_galoes_mix * 25.00

# Exibir os resultados

print("Quantidade de tinta necessaria: {:.2f} litros".format(litros_de_tinta))
print("Opção 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas {}".format(quantidade_latas_18))
print("Preço total: R${:.2f}".format(preco_latas_18))
print()
print("Opção 2: Comprar apenas galões de de 3,6 litros ")
print("Quantidade de galões: {}".format(quantidade_latas_36))
print("Preço total R${:.2f}".format(preco_galoes_36))
print()
print("Opção 3: Misturar latas e galões")
print("Quantidade de latas: {}, quantidade de galões: {}".format(quantidade_galoes_mix, quantidade_latas_mix))
print("Preço total: R${:.2f}".format(preco_mix))