###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Líquido
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura de dados
Bruto = float(input())

# Desconto de INSS
if (Bruto < 1045.00):
 INSS = Bruto * 0.075
elif (1045.00 <= Bruto < 2089.60):
 INSS = Bruto * 0.09
elif (2089.60 <= Bruto < 3134.40):
 INSS = Bruto * 0.12
elif (3134.40 <= Bruto < 6101.06):
 INSS = Bruto * 0.14
else:
 INSS = 6101.06 * 0.14

# Desconto de IR
if ((Bruto - INSS) < 1903.98):
 IR = 0.00
elif (1903.98 <= (Bruto - INSS) < 2826.65):
 IR = (Bruto - INSS) * 0.075 - 142.80
elif (2826.65 <= (Bruto - INSS) < 3751.05):
 IR = (Bruto - INSS) * 0.15 - 354.80
elif (3751.05 <= (Bruto - INSS) < 4664.68):
 IR = (Bruto - INSS) * 0.225 - 636.13
else:
 IR = (Bruto - INSS) * 0.275 - 869.36

# Saída de dados
Liquido = ((Bruto - INSS) - IR)

print("Bruto: R$", format(Bruto, ".2f").replace(".", ","))
print("INSS: R$", format(INSS, ".2f").replace(".", ","))
print("IR: R$", format(IR, ".2f").replace(".", ","))
print("Liquido: R$", format(Liquido, ".2f").replace(".", ","))
