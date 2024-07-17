################################################### (Tem outro jeito que eu estava fazendo, mas não terminei)
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura de dados
Linhas = int(input()) ## Quantidade de linhas vai ter o texto

Texto = [] ## Colocar em "" é uma "string"
for i in range(Linhas):
  T = input()
  T1 = T.lower().split(" ") ## Colocando tudo em minusculo e "separando" na lista através do espaço
  ## ".split()" já tira todos os caracteres em branco da frase (por exemplo: espaços, tabs (\t), \n)
  Texto.append(T1)
Texto = sum(Texto, []) ## Não sei o porquê, mas isso não fica como uma matriz, só uma lista de uma linha... 

Q_Palavras = int(input()) ## Quantidade de palavras para buscar

As_Palavras = []
for i in range(Q_Palavras):
  Palavra = input()  ## A palavra que deve ser buscada
  As_Palavras.append(Palavra)

# Processamento do texto
Pontuação = [".", ",", ":", ";", "!", "?"] ## Tirando as pontuações que podem atrapalhar
for p in Pontuação:
  for l in range(len(Texto)):
    Texto[l] = Texto[l].replace(p, "") ## Muda o que a gente quer (no caso a pontuação) para "nada"

T_Novo = str(Texto) ## Transformando elementos (no caso, cada palavra) da "lista" em uma "string"

# Saída de dados
for j in As_Palavras:
  P_Novo = j.lower()
  Ocorrencia = Texto.count(P_Novo) ## Quantidade de vezes que a palavra em si foi contada
  print("Palavra buscada:", j)
  print("Ocorrencia:", Ocorrencia)
  Parecida = T_Novo.count(P_Novo) ## Quantidade de vezes que a palavra em si e as parecidas foram contadas
  P_Similares = Parecida - Ocorrencia ## Só fica a quantidade de vezes que as palavras parecidas foram contadas
  print("Palavras similares:", P_Similares)
