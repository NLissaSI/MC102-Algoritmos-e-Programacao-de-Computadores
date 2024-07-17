###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura do hp dos lutadores
HP_Ryu = int(input())
HP_Ken = int(input())

# Leitura da sequência de golpes
Golpes_Ryu = 0
Golpes_Ken = 0

Dano = int(input())
while (HP_Ryu > 0) and (HP_Ken > 0): # Acho que o "and (HP_Ken > 0)" não fez nada... mas sei lá... Obs: o "and" funciona no while tbm, mas não sei o por quê de não estar fazendo nada, explicitamente... eu acho.
 if (Dano < 0): # Ken ataca
   Golpes_Ken = Golpes_Ken + 1
   HP_Ryu = HP_Ryu + (Dano)
   print("KEN APLICOU UM GOLPE:", - Dano)
   if (HP_Ryu > 0):
     print("HP RYU =", HP_Ryu)
     print("HP KEN =", HP_Ken)
   elif(HP_Ryu <= 0):
     print("HP RYU =", 0)
     print("HP KEN =", HP_Ken)
     break
 elif (Dano > 0): # Ryu ataca
   Golpes_Ryu = Golpes_Ryu + 1
   HP_Ken = HP_Ken - (Dano)
   print("RYU APLICOU UM GOLPE:", Dano)
   if(HP_Ken > 0): 
     print("HP RYU =", HP_Ryu)
     print("HP KEN =", HP_Ken)
   elif(HP_Ken <= 0):
     print("HP RYU =", HP_Ryu)
     print("HP KEN =", 0)
     break
 Dano = int(input())

# Impressão do vencedor e do número de golpes aplicados
if (HP_Ryu <= 0):
 print("LUTADOR VENCEDOR: KEN")
 print("GOLPES RYU =", Golpes_Ryu) 
 print("GOLPES KEN =", Golpes_Ken)
elif (HP_Ken <= 0):
 print("LUTADOR VENCEDOR: RYU")
 print("GOLPES RYU =", Golpes_Ryu) 
 print("GOLPES KEN =", Golpes_Ken)

=================================================== (Não sei se tem alguma diferença entre esses dois códigos)

###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Nathaly Lissa S. Izawa
# RA: 186028
###################################################

# Leitura do hp dos lutadores
HP_Ryu = int(input())
HP_Ken = int(input())

# Leitura da sequência de golpes
Golpes_Ryu = 0
Golpes_Ken = 0

Dano = int(input())
while (HP_Ryu > 0) and (HP_Ken > 0):
 if (Dano < 0): # Ken ataca
   Golpes_Ken = Golpes_Ken + 1
   HP_Ryu = HP_Ryu + (Dano)
   print("KEN APLICOU UM GOLPE:", - Dano)
   if (HP_Ryu > 0):
     print("HP RYU =", HP_Ryu)
     print("HP KEN =", HP_Ken)
   elif(HP_Ryu <= 0):
     print("HP RYU =", 0)
     print("HP KEN =", HP_Ken)
     break
 elif (Dano > 0): # Ryu ataca
   Golpes_Ryu = Golpes_Ryu + 1
   HP_Ken = HP_Ken - (Dano)
   print("RYU APLICOU UM GOLPE:", Dano)
   if(HP_Ken > 0): 
     print("HP RYU =", HP_Ryu)
     print("HP KEN =", HP_Ken)
   elif(HP_Ken <= 0):
     print("HP RYU =", HP_Ryu)
     print("HP KEN =", 0)
     break
 Dano = int(input())

# Impressão do vencedor e do número de golpes aplicados
if (HP_Ryu <= 0):
 print("LUTADOR VENCEDOR: KEN")
 print("GOLPES RYU =", Golpes_Ryu) 
 print("GOLPES KEN =", Golpes_Ken)
elif (HP_Ken <= 0):
 print("LUTADOR VENCEDOR: RYU")
 print("GOLPES RYU =", Golpes_Ryu) 
 print("GOLPES KEN =", Golpes_Ken)
