###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura de dados
  # Leitura do tabuleiro
    # Dica: use a função list() para transformar uma string numa lista de caracteres
altu_tabuleiro, larg_tabuleiro = [int(x) for x in input().split()] ## O tamanho do tabuleiro

Tabuleiro = [] ## Tabuleiro original
N_Tabuleiro = [] ## Tabuleiro em que os "*" são ".", fica parecido com a peça
for i in range(altu_tabuleiro):
  LT = input().replace("*", "* ").replace(".", ". ")
  Tabuleiro.append(LT.split())
  N_Tabuleiro.append(LT.replace(".", "#").replace("*", ".").split())

  # Leitura da peça
    # Dica: use a função list() para transformar uma string numa lista de caracteres
altu_peca, larg_peca = [int(x) for x in input().split()] ## O tamanho da peça

Peça = []
for p in range(altu_peca):
  LP = input().replace(".", ". ").replace("#", "# ")
  Peça.append(LP.split())

# Impressão da configuração atualizada do tabuleiro
for k in range(altu_tabuleiro):
  for j in range(larg_tabuleiro - larg_peca + 1):
    m = 0
    for i in range(altu_peca):    
      bloquinho = "".join(N_Tabuleiro[k+i][j:(j + larg_peca)])
      pecinha = "".join(Peça[i])
      
      if bloquinho == pecinha:
        m += 1
      else:
        break
    if m == altu_peca:
      break
  if m == altu_peca:
    break
## Se o m == altura_peca, então quer dizer que a peça se encaixou no tabuleiro

tabuleiro = Tabuleiro.copy()
for w in range(len(tabuleiro)):
  tabuleiro[w] = Tabuleiro[w].copy()

if m == altu_peca:
  for u in range(k, k + altu_peca): 
    for n in range(j, j + larg_peca): 
      if tabuleiro[u][n] == ".":
        tabuleiro[u][n] = "#"
  status_do_jogo = "O jogo deve continuar"
elif m != altu_peca:
  status_do_jogo = "Fim de jogo"

for linha in tabuleiro:
	print("".join(linha))

# Impressão do status do jogo
print(status_do_jogo)


# (VERSÃO COM TODAS AS ANOTAÇÕES)
# Leitura de dados
  # Leitura do tabuleiro
    # Dica: use a função list() para transformar uma string numa lista de caracteres
altu_tabuleiro, larg_tabuleiro = [int(x) for x in input("Qual é a altura e a largura do tabuleiro? ").split()] ## O tamanho do tabuleiro
print("Altura é", altu_tabuleiro) ## APAGAR DEPOIS
print("Largura é", larg_tabuleiro) ## APAGAR DEPOIS

Tabuleiro = [] ## Tabuleiro original
N_Tabuleiro = [] ## Tabuleiro em que os "*" são ".", fica parecido com a peça
for i in range(altu_tabuleiro):
  LT = input().replace("*", "* ").replace(".", ". ")
  Tabuleiro.append(LT.split())
  N_Tabuleiro.append(LT.replace(".", "#").replace("*", ".").split())
  
print("Tabuleiro é", Tabuleiro, "\n") ## APAGAR DEPOIS
#print("N_Tabuleiro", N_Tabuleiro)
for i in N_Tabuleiro:
  print("".join(i))

  # Leitura da peça
    # Dica: use a função list() para transformar uma string numa lista de caracteres
altu_peca, larg_peca = [int(x) for x in input("Qual é a altura e a largura da peça? ").split()] ## O tamanho da peça
print("Altura é", altu_peca) ## APAGAR DEPOIS
print("Largura é", larg_peca) ## APAGAR DEPOIS

Peça = []
for p in range(altu_peca):
  LP = input().replace(".", ". ").replace("#", "# ")
  Peça.append(LP.split())

#print("Peça é", Peça) ## APAGAR DEPOIS
print()
for i in Peça:
  print("".join(i))

# Impressão da configuração atualizada do tabuleiro
for k in range(altu_tabuleiro):
  for j in range(larg_tabuleiro - larg_peca + 1):
    m = 0
    for i in range(altu_peca):    
      bloquinho = "".join(N_Tabuleiro[k+i][j:(j + larg_peca)])
      pecinha = "".join(Peça[i])
      print(k, "\t", j, "\t", bloquinho, "\t", pecinha, end = "\t")
      
      if bloquinho == pecinha:
        m += 1
      else:
        break
    print(m)  
    if m == altu_peca:
      break
  if m == altu_peca:
    break
## Se o m == altura_peca, então quer dizer que a peça se encaixou no tabuleiro
print(k, "\t", j, "\n")

tabuleiro = Tabuleiro.copy()
for w in range(len(tabuleiro)):
  tabuleiro[w] = Tabuleiro[w].copy()

if m == altu_peca:
  for u in range(k, k + altu_peca): #k
    for n in range(j, j + larg_peca): #j
      if tabuleiro[u][n] == ".":
        print(u, "\t", n)
        tabuleiro[u][n] = "#"

  status_do_jogo = "O jogo deve continuar"
elif m != altu_peca:
  status_do_jogo = "Fim de jogo"

for linha in tabuleiro:
	print("".join(linha))

# Impressão do status do jogo
print(status_do_jogo)
