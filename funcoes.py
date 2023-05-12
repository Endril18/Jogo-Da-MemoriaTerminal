#imports
import random
import os

#criação do deck
def deck(naipe, figura):
  novaLista = []
  for i in range(10):
    cartaNova = random.choice(naipe) + random.choice(figura)
    while(cartaNova in novaLista):
      cartaNova = random.choice(naipe) + random.choice(figura)
    novaLista.append(cartaNova)
  novaLista += novaLista
  random.shuffle(novaLista) #embaralhamento do deck
  return novaLista

#divisão das linhas
def tabuleiro(lista):
  tabuleiro = []
  tabuleiro.append(lista[0:5])
  tabuleiro.append(lista[5:10])
  tabuleiro.append(lista[10:15])
  tabuleiro.append(lista[15:20])
  return tabuleiro

#igualdade das cartas
def CartaIgualdade(deckComparado, linha1, linha2, coluna1, coluna2):
  if(deckComparado[linha1][coluna1] == deckComparado[linha2][coluna2]):
    return True
  return False

#comparação de cartas escolhidas e pontuação
def testeCartas(deckComparado, linha1, linha2, coluna1, coluna2):
  figura_i = 1
  naipe_i = 0
  pontos = 0
  if(deckComparado[linha1][coluna1][figura_i] == deckComparado[linha2][coluna2][figura_i]):
    if(deckComparado[linha1][coluna1] == deckComparado[linha2][coluna2]):
      pontos = 50
    else:
      pontos = 20
    return pontos
  elif(deckComparado[linha1][coluna1][naipe_i] == deckComparado[linha2][coluna2][naipe_i]):
    pontos = 30
    return pontos
  return pontos

#exibir a carta que o jogador escolheu
def exibirCartaEscolhida(deckReal, deckEscondido, linha, coluna):
  valorReal = deckReal[linha][coluna]
  deckEscondido[linha][coluna] = valorReal
  return deckEscondido

#remover a carta que o jogador escolheu
def removerCartaEscolhida(deckComAmostras, linha1, coluna1, linha2, coluna2):
  preencher = "x"
  deckComAmostras[linha1][coluna1] = preencher
  deckComAmostras[linha2][coluna2] = preencher
  return deckComAmostras

#verificar se todas foram viradas
def todasViradas(deckReal, deckEscondido):
  if(deckReal == deckEscondido):
    return True
  return False

#vecedor da partida 
def vencedor(pontos1, pontos2, jogador1, jogador2):
  resultado = ""
  if(pontos1 > pontos2):
    resultado = jogador1
  elif(pontos2 > pontos1):
    resultado  = jogador2
  else:
    resultado = "empate"
  return resultado
    
#apagador
def limpeza():
  if(os.name == "nt"):
    os.system("cls")
  else:
    os.system("clear")