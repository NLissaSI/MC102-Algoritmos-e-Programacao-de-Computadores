###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################
 (VERSÃO SEM AS MILHARES DE NOTAÇÕES)
## Algumas funções...
def compara_p(palavra, trecho):
  Lista_ast = [] ## Posições com asterisco
  for h in range(len(trecho)):
    if trecho[h] == "*":
      Lista_ast.append(int(h))

  for h in (Lista_ast[::-1]): ## Lista do "último pro primeiro"
    trecho = trecho[:h] + trecho[(h + 1):] ## Removendo o asterisco do trecho
    palavra = palavra[:h] + palavra[(h + 1):] ## Removendo a letra que está na mesma posição que o asterisco

  if trecho == palavra or trecho[::-1] == palavra:
    return True
  else:
    return False
  
def Transp_matriz(m):
  MT = []
  for c in range(len(m[0])): ## Colunas na matriz original
    linha_t = []
    for l in range(len(m)): ## Linhas na matriz original
      linha_t.append(m[l][c])
    MT.append(linha_t) 
  return MT

# Leitura da matriz
  # Dica: use linha.isdigit(), linha.split() e matriz.append()
  # para processar a entrada e armazenar a matriz de caracteres

Malha = [] ## O formará "tabuleiro" do caça - palavras
Linha = input()
Malha.append(Linha.split())

while Linha.isdigit() == False:
  Linha = input() ## As linhas que formam o tabuleiro
  if Linha.isdigit() == True: ## Numero de palavras
    N = Linha
  else:
    Malha.append(Linha.split())

N_Malha = Malha.copy()
for w in range(len(N_Malha)):
  N_Malha[w] = Malha[w].copy()

# Leitura e processamento das palavras
Palavras = []
dic = {}
for i in range(int(N)):
  P = input()
  dic[P] = {"Ocorrencias": 0}
  Palavras.append(P)
for palavra in Palavras: ## Horizontal
  for i in range(len(Malha)): ## Linha
    for j in range(len(Malha[i]) - len(palavra) + 1): ## Coluna
      if (compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[i][k] = N_Malha[i][k].upper()

M_Transp = Transp_matriz(Malha)

for palavra in Palavras: ## Vertical
  for i in range(len(M_Transp)): ## Linha
    for j in range(len(M_Transp[i]) - len(palavra) + 1): ## Coluna
      if (compara_p(palavra, "".join(M_Transp[i][j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[k][i] = N_Malha[k][i].upper()

## Diagonal (esquerda cima para direita baixo) indo da "metade" para direita
diagonale = []
a = 0
for b in range(len(Malha[0])): 
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in range(a,len(Malha)):
    vb1.append(b1)
    va1.append(a1)
    diagonal.append(Malha[a1][b1])
    b1 += 1
    if b1 >= len(Malha[0]) or a1 >= len(Malha):
      break

  diagonale.append(diagonal)

  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Coluna
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[va1[k]][vb1[k]] = N_Malha[va1[k]][vb1[k]].upper()

## Diagonal (esquerda cima para direita baixo) indo da "metade" para a esquerda
a = 0
for b in range(len(Malha)):
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in range(a,len(Malha[0])):
    vb1.append(b1)
    va1.append(a1)
    diagonal.append(Malha[b1][a1])
    b1 += 1
    if b1 >= len(Malha) or a1>= len(Malha[0]):
      break
  
  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Coluna
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
        if diagonal in diagonale or diagonale[::-1] in diagonale:
          continue
        else:
          dic[palavra]["Ocorrencias"] += 1
          for k in range(j, (j + len(palavra)) ):
            N_Malha[vb1[k]][va1[k]] = N_Malha[vb1[k]][va1[k]].upper()

## Diagonal (direita cima para esquerda baixo) indo da direita baixo para esquerda cima até a metade
diagonald = []
a = 0
for b in reversed( range (len(Malha[0]) ) ): ## Quantidade de colunas
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in reversed( range (len(Malha) ) ):
    vb1.append(b1)
    va1.append(a1)
    diagonal.append(Malha[a1][b1])
    b1 += 1
    if b1 >= len(Malha[0]) or a1 >= len(Malha):
      break

  diagonald.append(diagonal)

  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Coluna
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[va1[k]][vb1[k]] = N_Malha[va1[k]][vb1[k]].upper()

## Diagonal (direita cima para esquerda baixo) indo da esquerda cima para direita baixo até a metade
a = 0
for b in reversed( range (len(Malha[0]) ) ):
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in ( range (a,len(Malha) ) ):
    vb1.append(b1)
    va1.append(a1)
    if b1 < 0:
      continue
    else:
      diagonal.append(Malha[a1][b1])
      b1 -= 1

  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Coluna
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
        if diagonal in diagonald or diagonal[::-1] in diagonald:
          continue
        else:
          dic[palavra]["Ocorrencias"] += 1
          for k in range(j, (j + len(palavra)) ):
            N_Malha[va1[k]][vb1[k]] = N_Malha[va1[k]][vb1[k]].upper()

# Saída dos dados
print("-" * 40)
print("Lista de Palavras")
print("-" * 40)
for palavra in Palavras:
  print("Palavra:", palavra)
  print("Ocorrencias:", dic[palavra]["Ocorrencias"])
  print("-" * 40)

# Impressão da matriz
for linha in N_Malha:
  print(" ".join(linha)) ## O tabuleiro em si. Transforma uma lista em uma "string" MESMO (não o elemento que "linha" está apontando)



(VERSÃO COM TUDO)

###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

def compara_p(palavra, trecho):
  Lista_ast = [] ## Posições com asterisco
  for h in range(len(trecho)):
    if trecho[h] == "*":
      Lista_ast.append(int(h))
  #print(palavra, trecho) ## (APAGAR DEPOIS)

  for h in (Lista_ast[::-1]): ## Lista do "último pro primeiro"
    trecho = trecho[:h] + trecho[(h + 1):] ## Removendo o asterisco do trecho
    palavra = palavra[:h] + palavra[(h + 1):] ## Removendo a letra que está na mesma posição que o asterisco
  #print("->", palavra, trecho) ## (APAGAR DEPOIS)

  if trecho == palavra or trecho[::-1] == palavra:
    return True
  else:
    return False
  
def Transp_matriz(m):
  MT = []
  for c in range(len(m[0])): ## Colunas na matriz original
    linha_t = []
    for l in range(len(m)): ## Linhas na matriz original
      linha_t.append(m[l][c])
    MT.append(linha_t) 
  return MT

'''
  M_Transp = []
  for c in range(len(Malha[0])): ## Colunas na matriz original
    linha_t = []
    for l in range(len(Malha)): ## Linhas na matriz original
      linha_t.append(Malha[l][c])
    M_Transp.append(linha_t) 

M_Transp =
  [ [ Malha[l][c] for l in range( len(Malha) ) ] for c in range( len(Malha[0]) ) ] ## Transpoem (?) a matriz...
'''

# Leitura da matriz
  # Dica: use linha.isdigit(), linha.split() e matriz.append()
  # para processar a entrada e armazenar a matriz de caracteres

Malha = [] ## O formará "tabuleiro" do caça - palavras
Linha = input("Primeira linha: ") ## (APAGAR DEPOIS O QUE TEM DENTRO)
Malha.append(Linha.split())

while Linha.isdigit() == False: ## Não sei pq tem que ser "False" pra funcinar, mas funciona...
  Linha = input("Próxima linha: ") ## As linhas que formam o tabuleiro
  ## N = Linha if Linha.isdigit() else Malha.append(Linha.split())
  ## (APAGAR DEPOIS O QUE TEM DENTRO)
  if Linha.isdigit() == True: ## Numero de palavras
    N = Linha
  else:
    Malha.append(Linha.split())

'''
print(Malha) ## A matriz que contém as letras (APAGAR DEPOIS)

for linha in Malha: ## Verificando o tabuleiro (APAGAR DEPOIS)
  print(" ".join(linha)) ## O tabuleiro em si (esse negócio está lá no fim também). Transforma uma lista em uma "string" MESMO (não o elemento que "linha" está apontando). Pelo menos o tipo é "str"...
'''

N_Malha = Malha.copy()
for w in range(len(N_Malha)):
  N_Malha[w] = Malha[w].copy()

# Leitura e processamento das palavras
Palavras = []
dic = {}
for i in range(int(N)):
  P = input("Qual palavra? ") ## (APAGAR DEPOIS O QUE TEM DENTRO)
  dic[P] = {"Ocorrencias": 0}
  Palavras.append(P) ## Tipo "str" (?)...

for palavra in Palavras: ## Horizontal
  for i in range(len(Malha)): ## Linha
    for j in range(len(Malha[i]) - len(palavra) + 1): ## Não ocorrer o problema de andar no zero ## Coluna
      ## print("".join(Malha[i][j:(j + len(palavra))]), end = " ") ## O negócio que anda em bloquinhos fixos
      ## print(compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) ))
      if (compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[i][k] = N_Malha[i][k].upper()
      
#print(N_Malha) ## (APAGAR DEPOIS) Em forma de lista

M_Transp = Transp_matriz(Malha)

'''
print() ## (APAGAR DEPOIS)
for i in M_Transp: ## (APAGAR DEPOIS)
  print(" ". join(i))
print() ## (APAGAR DEPOIS)
'''

for palavra in Palavras: ## Vertical
  for i in range(len(M_Transp)): ## Linha
    for j in range(len(M_Transp[i]) - len(palavra) + 1): ## Não ocorrer o problema de andar no zero ## Coluna
      ## print("".join(Malha[i][j:(j + len(palavra))]), end = " ") ## O negócio que anda em bloquinhos fixos
      ## print(compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) ))
      if (compara_p(palavra, "".join(M_Transp[i][j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[k][i] = N_Malha[k][i].upper()

## Diagonal (esquerda cima para direita baixo) indo da "metade" para direita
diagonale = []
a = 0
for b in range(len(Malha[0])): 
  print(a," ",b," ",Malha[a][b])
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in range(a,len(Malha)):
    vb1.append(b1)
    va1.append(a1)
    print(a," ",b," ",a1," ",b1, " ", len(Malha[0]), " ", len(Malha), end = "\t")
    print(Malha[a][b]," ",Malha[a1][b1])
    print(a," ",b," ",Malha[a][b]," ",a1," ",b1," ",Malha[a1][b1])
    diagonal.append(Malha[a1][b1])
    b1 += 1
    if b1 >= len(Malha[0]) or a1 >= len(Malha):
      break
  print(diagonal)

  diagonale.append(diagonal)

  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Não ocorrer o problema de andar no zero ## Coluna
    ## print("".join(Malha[i][j:(j + len(palavra))]), end = " ") ## O negócio que anda em bloquinhos fixos
    ## print(compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) ))
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[va1[k]][vb1[k]] = N_Malha[va1[k]][vb1[k]].upper()

print(diagonale, "\n")

## Sera que se eu fizer dois vetores gerais (um para cada diagonal X) isso resolve o problema?
print()

## Diagonal (esquerda cima para direita baixo) indo da "metade" para a esquerda
a = 0
for b in range(len(Malha)):
  print(b," ",a," ",Malha[b][a])
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in range(a,len(Malha[0])):
    vb1.append(b1)
    va1.append(a1)
    #print(b," ",a," ",b1," ",a1, " ", len(Malha[0]), end = "\t")
    #print(Malha[b][a]," ",Malha[b1][a1])
    #print(a," ",b," ",Malha[a][b]," ",a1," ",b1," ",Malha[a1][b1])
    diagonal.append(Malha[b1][a1])
    b1 += 1
    if b1 >= len(Malha) or a1>= len(Malha[0]):
      break
  print(diagonal)
  
  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Não ocorrer o problema de andar no zero ## Coluna
    ## print("".join(Malha[i][j:(j + len(palavra))]), end = " ") ## O negócio que anda em bloquinhos fixos
    ## print(compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) ))
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
 
        if diagonal in diagonale or diagonale[::-1] in diagonale: ## if len(Malha) < len(Malha[0]):
          continue
        else:
 
          dic[palavra]["Ocorrencias"] += 1
          for k in range(j, (j + len(palavra)) ):
            N_Malha[vb1[k]][va1[k]] = N_Malha[vb1[k]][va1[k]].upper() ## Alterei a ordem, verificar depois com os exemplos anteriores...

print()
## Diagonal (direita cima para esquerda baixo) indo da direita baixo para esquerda cima até a metade
diagonald = []
a = 0
for b in reversed( range (len(Malha[0]) ) ): ## Quantidade de colunas
  print(a," ",b," ",Malha[a][b])
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in reversed( range (len(Malha) ) ):
    vb1.append(b1)
    va1.append(a1)
    print(a," ",b," ",a1," ",b1, " ", len(Malha[0]), end ="\t")
    print(Malha[a][b]," ",Malha[a1][b1])
    print(a," ",b," ",Malha[a][b]," ",a1," ",b1," ",Malha[a1][b1])
    diagonal.append(Malha[a1][b1])
    b1 += 1
    if b1 >= len(Malha[0]) or a1 >= len(Malha):
      break
  print(diagonal)

  diagonald.append(diagonal)

  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Não ocorrer o problema de andar no zero ## Coluna
    ## print("".join(Malha[i][j:(j + len(palavra))]), end = " ") ## O negócio que anda em bloquinhos fixos
    ## print(compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) ))
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
        dic[palavra]["Ocorrencias"] += 1
        for k in range(j, (j + len(palavra)) ):
          N_Malha[va1[k]][vb1[k]] = N_Malha[va1[k]][vb1[k]].upper()

print(diagonald, "\n")

print()

## Diagonal (direita cima para esquerda baixo) indo da esquerda cima para direita baixo até a metade
a = 0
for b in reversed( range (len(Malha[0]) ) ):
  print(b," ",a, end="\t")
  print(Malha[a][b])
  diagonal = []
  vb1 = []
  va1 = []
  b1 = b
  for a1 in ( range (a,len(Malha) ) ):
    vb1.append(b1)
    va1.append(a1)
    print(a," ",b," ",b1," ",a1, " ", len(Malha[0]), end = "\t")
    print(Malha[a][b]," ",Malha[a1][b1])
    print(a," ",b," ",Malha[a][b]," ",a1," ",b1," ",Malha[a1][b1])
    if b1 < 0:
      continue
    else:
      diagonal.append(Malha[a1][b1])
      b1 -= 1
  print(diagonal)

  for palavra in Palavras:
    for j in range(len(diagonal) - len(palavra) + 1): ## Não ocorrer o problema de andar no zero ## Coluna
    ## print("".join(Malha[i][j:(j + len(palavra))]), end = " ") ## O negócio que anda em bloquinhos fixos
    ## print(compara_p(palavra, "".join(Malha[i][j:(j + len(palavra))]) ))
      if (compara_p(palavra, "".join(diagonal[j:(j + len(palavra))]) )):
 
        if diagonal in diagonald or diagonal[::-1] in diagonald: ## if len(Malha) < len(Malha[0]):
          continue
        else:
 
          dic[palavra]["Ocorrencias"] += 1
          for k in range(j, (j + len(palavra)) ):
            N_Malha[va1[k]][vb1[k]] = N_Malha[va1[k]][vb1[k]].upper()

# Saída dos dados
print("-" * 40)
print("Lista de Palavras")
print("-" * 40)
for palavra in Palavras:
  print("Palavra:", palavra)
  print("Ocorrencias:", dic[palavra]["Ocorrencias"])
  print("-" * 40)

# Impressão da matriz
for linha in N_Malha:
  print(" ".join(linha)) ## O tabuleiro em si. Transforma uma lista em uma "string" MESMO (não o elemento que "linha" está apontando)

