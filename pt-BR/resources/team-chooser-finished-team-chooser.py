#!/bin/python3

from random import choice

#cria uma lista de jogadores vindos de um arquivo
jogadores= []
arquivo= open('jogadores.txt', 'r')
jogadores = arquivo.read().splitlines()
print('Jogadores:', jogadores)

#cria uma lista com as casas dos jogadores de um arquivo
nomesCasas = []
arquivo = open('nomesCasas.txt', 'r')
nomesCasas = file.read().splitlines()
print('Nome das Casas:', nomesCasas)

#create empty team lists
teamA = []
teamB = []

#loop until there are no players left
while len(players) > 0:
  
  #choose a random player for team A
  playerA = choice(players)
  teamA.append(playerA)
  #remove the player from the players list
  players.remove(playerA)
  
  #break out of the loop if there are no players left
  if players == []: 
    break
  
  #choose a random player for team B
  playerB = choice(players)
  teamB.append(playerB)
  #remove the player from the players list
  players.remove(playerB)

#choose random team names for the 2 teams
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#print the teams
print('\nHere are your teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)