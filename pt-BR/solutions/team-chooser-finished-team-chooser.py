#!/bin/python3

from random import choice

#cria uma lista de jogadores a partir de um arquivo
jogadores= []
arquivo= open('jogadores.txt', 'r')
jogadores = arquivo.read().splitlines()
print('Jogadores:', jogadores)

#cria uma lista de nomes de times a partir de um arquivo
nomesTimes = []
arquivo = open('nomesTimes.txt', 'r')
nomesTimes = arquivo.read().splitlines()
print('Nome de Times: ', nomesTimes)

#cria listas de equipes vazias
timeA = []
timeB = []

#loop até que não tenha mais jogadores
while len(jogadores) > 0:
  
  # escolhe um jogador aleatório para o time A
  jogadorA = choice(jogadores)
  timeA.append(jogadorA)
  #remove o jogador da lista de jogadores
  jogadores.remove(jogadorA)
  
  #encerra o loop caso não haja mais jogadores
  if jogadores == []: 
    break
  
  # escolhe um jogador aleatório para o time B
  jogadorB = choice(jogadores)
  timeB.append(jogadorB)
  #remove o jogador da lista de jogadores
  jogadores.remove(jogadorB)

# escolhe nomes aleatórios para as 2 equipes
nomeTimeA = choice(nomesTimes)
nomesTimes.remove(nomeTimeA)
nomeTimeB = choice(nomesTimes)
nomesTimes.remove(nomeTimeB)

#mostra os times
print ('\nAqui estão seus times:\n')
print (nomeTimeA, timeA)
print(nomeTimeB, timeB)