#imports
import time
import funcoes

#pontos
pt1 = 0
pt2 = 0
ptJogada1 = 0
ptJogada2 = 0

#deck
naipe = ["C", "O", "E", "P"]
figura = ["A", "J", "Q", "K"]

deck_completo = funcoes.deck(naipe, figura)  #criação do deck
tabuleiro_completo = funcoes.tabuleiro(deck_completo)  #criação de sublistas

#tabuleiro escondido
deckEscondido = ["x"] * 20
tabuleiro_escondido = funcoes.tabuleiro(deckEscondido)  #criação de sublistas
print("﹤", "▬" * 20, "﹥")
print("\n    Tabuleiro Escondido\n")
print("﹤", "▬" * 20, "﹥", "\n")
for i in range(len(tabuleiro_escondido)):  #mostrar tabuleiro escondido
  print(tabuleiro_escondido[i])

#regras do jogo
print(
  "\nInsira apenas valores como:\nPara Linhas: [1][2][3][4]\nPara Colunas: [1][2][3][4][5]\n"
)
print(
  "➢ Achando duas cartas iguais você ganha 50 pontos\n➢ Achando duas cartas com fíguras iguais você ganha 20 pontos\n➢ Achando duas cartas com naipes iguais você ganha 30 pontos\n"
)

#jogadores
jogador1_nome = input("➢ Digite o nome do primeiro jogador: ")
jogador2_nome = input("➢ Digite o nome do segundo jogador: ")

#escolha de cartas
jogadas = 1 #contador de rodadas
rodadas = 0 #variável de controle
jogador = jogador1_nome 
while (rodadas <= 10 or funcoes.todasViradas(tabuleiro_completo, tabuleiro_escondido == False)):
  for i in range(2):
    linha2 = int(input(f"\n- {jogador} - \nInforme uma linha: "))
    coluna2 = int(input(f"\n- {jogador} - \nInforme uma coluna: "))
    print("\n")

    #verificar se já foi utilizada
    while (linha2 < 1) or (linha2 > 4) or (coluna2 < 1) or (coluna2 > 5):
      print("Você não pode fazer essa jogada!")
      linha2 = int(input(f"\n- {jogador} - \nInforme novamente uma linha: "))
      coluna2 = int(input(f"\n- {jogador} - \nInforme novamente uma coluna: "))

    #ajeitando indices
    linha2 -= 1
    coluna2 -= 1
    print("\n")

    while (tabuleiro_escondido[linha2][coluna2] != 'x'):
      print("Você não pode fazer essa jogada!")
      linha2 = int(input(f"\n- {jogador} - \nInforme novamente uma linha: "))
      coluna2 = int(input(f"\n- {jogador} - \nInforme novamente uma coluna: "))
      linha2 -= 1
      coluna2 -= 1
      print("\n")

    #guardando posição da primeira carta escolhida
    if (i == 0):
      linha1 = linha2
      coluna1 = coluna2

    #mostrar carta escolhida
    tabuleiroCartasEscolhidas = funcoes.exibirCartaEscolhida(tabuleiro_completo, tabuleiro_escondido, linha2, coluna2)
    for c in range(len(tabuleiro_completo)):
      print(funcoes.exibirCartaEscolhida(tabuleiro_completo, tabuleiro_escondido,linha2, coluna2)[c])

  #pontuação
  if (jogador1_nome == jogador):
    ptJogada1 = funcoes.testeCartas(tabuleiro_completo, linha1, linha2,coluna1, coluna2)
    pt1 += ptJogada1
    print(f"\n{jogador}, nessa rodada você fez: {ptJogada1} pontos!\n")
    print(f"\n{jogador}, você acumulou ao todo {pt1} pontos!\n")
  elif (jogador2_nome == jogador):
    ptJogada2 = funcoes.testeCartas(tabuleiro_completo, linha1, linha2, coluna1, coluna2)
    pt2 += ptJogada2
    print(f"\n{jogador}, nessa rodada você fez: {ptJogada2} pontos!\n")
    print(f"\n{jogador}, você acumulou ao todo {pt2} pontos!\n")

  #escondendo tabuleiro
  if(rodadas < 10):
    if (funcoes.CartaIgualdade(tabuleiro_completo, linha1, linha2, coluna1, coluna2) == False):
      print("\nÉ a vez do outro jogador.")
      time.sleep(3)
      print("Pressione Enter")
      enter = input()
      time.sleep(3)
      funcoes.limpeza()
      print("\nEscondendo tabuleiro...\n")
      time.sleep(3)
      removendoEscolha = funcoes.removerCartaEscolhida(tabuleiro_escondido,linha1, coluna1, linha2,coluna2)
      for i in range(len(tabuleiro_escondido)):
        print(removendoEscolha[i])
    else:
      print("\nÉ a vez do outro jogador.")
      time.sleep(3)
      print("Pressione Enter")
      enter = input()
      time.sleep(3)

  #variável de controle
  rodadas += 1

  #rodada do jogo
  if (rodadas < 10):
    print("\n- Você está na rodada: ", rodadas)
  else:
    print("\n- FINAL FIGHT -\n")

  #mudança de nome do jogador
  if (rodadas % 2 == 0):
    jogador = jogador1_nome
  else:
    jogador = jogador2_nome
    jogadas += 1

#ganhador da partida
print("﹤", "▬" * 20, "﹥")
print(f"\nO ganhador dessa partida é {funcoes.vencedor(pt1, pt2, jogador1_nome, jogador2_nome)}\n")
time.sleep(3)
print("     Jogo Finalizado\n")
print("﹤", "▬" * 20, "﹥")





