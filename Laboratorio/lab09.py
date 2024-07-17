#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Copa do Mundo de Futebol
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
#####################################################

# Leitura da lista de seleções
Seleções = [] ## Nomes dos paises
dic = {} ## Dicionarios não são acessados por indices, mas por "Key"
for i in range(16): ## Voltar para 16
  Seleção = input() ## Nome do país (de onde veio o time)
  Seleções.append(Seleção) 
  ## Para a seleção adicionada, ele vai criar um dicionario para elas (é preciso atualizar essas informações), ele vai simplesmente sobreescrever o que tinha antes
  dic[Seleção] = {"partidas": 0, ## Key : Value
                  "vitorias": 0,
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}

# Leitura das partidas e processamento dos dados
for l in range(16):
  Informações = input().replace("(", "( ").replace(")", " )").split()
  if Informações[4] == "(": ## Se tiver penalti
    i = 5
    dic[Informações[0]]["penaltis"] += 1
    dic[Informações[4 + i]]["penaltis"] += 1
    if int(Informações[5]) > int(Informações[7]):
      dic[Informações[0]]["vitorias"] += 1
      dic[Informações[4 + i]]["derrotas"] += 1
    elif int(Informações[5]) < int(Informações[7]):
      dic[Informações[4 + i]]["vitorias"] += 1
      dic[Informações[0]]["derrotas"] += 1
  else: ## Se não tiver penalti
    i = 0
    dic[Informações[0]]["normal"] += 1
    dic[Informações[4 + i]]["normal"] += 1
    if int(Informações[1]) > int(Informações[3]):
      dic[Informações[0]]["vitorias"] += 1
      dic[Informações[4 + i]]["derrotas"] += 1
    elif int(Informações[1]) < int(Informações[3]):
      dic[Informações[4 + i]]["vitorias"] += 1
      dic[Informações[0]]["derrotas"] += 1

  dic[Informações[0]]["partidas"] += 1 ## Primeiro país da partida
  dic[Informações[0]]["marcados"] += int(Informações[1]) ## Quantidade de gols que o primeiro país marcou
  dic[Informações[0]]["sofridos"] += int(Informações[3]) ## Quantidade de gols que o primeiro país sofreu
  dic[Informações[4 + i]]["partidas"] += 1 ## Segundo país da partida
  dic[Informações[4 + i]]["marcados"] += int(Informações[3]) ## Quantidade de gols que o segundo país marcou
  dic[Informações[4 + i]]["sofridos"] += int(Informações[1]) ## Quantidade de gols que o segundo país sofreu

# Saída de dados
for Seleção in Seleções:
  print("-" * 50)
  print("Pais:", Seleção)
  print("Partidas:", dic[Seleção]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[Seleção]["normal"])
  print("Partidas decicidas nos penaltis:", dic[Seleção]["penaltis"])
  print("Vitorias:", dic[Seleção]["vitorias"])
  print("Derrotas:", dic[Seleção]["derrotas"])
  print("Gols marcados:", dic[Seleção]["marcados"])
  print("Gols sofridos:", dic[Seleção]["sofridos"])

for l in Seleções:
  if dic[l]["derrotas"] == 0:
    Campeão = l

print("-" * 50)
print("Pais campeao:", Campeão)
print("-" * 50)
