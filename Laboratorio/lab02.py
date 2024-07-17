###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura de dados
x = int(input())
t = int(input())
v_1 = float(input())
v_2 = float(input())

# Cálculo dos tempos de viagem
t_1 = (x / v_1)
t_2 = (x / v_2) + (t / 60)

# Impressão da resposta
print(t_1 < t_2)
