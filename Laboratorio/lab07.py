###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura de dados
Quantidade = int(input()) # Quantidade de notas que tem o aluno

Notas = []
for i in range(Quantidade):
  N = float(input())
  Notas.append(N)

Pesos = []
for j in range(Quantidade):
  P = int(input())
  Pesos.append(P)

# Cálculo da média ponderada dos laboratórios
Peso = 0
for l in Pesos:
  Peso = Peso + l

Soma = 0
for i in range(len(Notas)):
  Soma = Soma + Notas[i - 1] * Pesos[i - 1]

Média = Soma / Peso

print("Media laboratorios:", format(Média, ".1f").replace(".", ","))

# Verificação da situação do aluno
if Média >= 5: # Caso o aluno tenha sido aprovado por nota
  print("Situacao: Aprovado por nota")
  Nota_Final = Média
elif Média < 2.5: # Caso o aluno tenha sido reprovado por nota
  print("Situacao: Reprovado por nota")
  Nota_Final = Média
else: # Cálculo da nota do exame, caso o aluno tenha ido para o exame
  Lab_Exame = int(input())
  Labs = []
  for i in range(Lab_Exame):
    L = int(input())
    Labs.append(L)

  Notas_Exame = []
  for j in range(Lab_Exame):
    N_E = float(input())
    Notas_Exame.append(N_E)

  Peso_Exame = 0
  for l in Labs:
    Peso_Exame = Peso_Exame + Pesos[l - 1]

  Soma_Exame = 0
  for i in range(len(Notas_Exame)):
    Soma_Exame = Soma_Exame + Notas_Exame[i - 1] * Pesos[Labs[i - 1] - 1]

  Média_Exame = Soma_Exame / Peso_Exame

  Nova_Média = (Média + Média_Exame) / 2

  if Nova_Média > 5: # Caso o aluno tenha sido aprovado no exame
    print("Situacao: Aprovado no exame")
    Nota_Final = 5
  else: # Caso o aluno tenha sido repravado no exame
    print("Situacao: Reprovado no exame")
    Nota_Final = Nova_Média

# Saída de dados
print("Nota final:", format(Nota_Final, ".1f").replace(".", ","))
