#!/bin/python3

from random import choice

#crea un elenco di giocatori da un file
giocatori = []
file = open('giocatori.txt', 'r')
giocatori = (file.read().splitlines())
print('Giocatori:', giocatori)

#crea un elenco di nomi di team da un file
teamNomi = []
file = open('teamNomi.txt', 'r')
teamNomi = file.read().splitlines()
print('Nome delle squadre:', teamNomi)

#crea elenchi vuoti di team
teamA = []
teamB = []

#esegui ciclicamente fino a quando non ci sono più giocatori
while len(giocatori) > 0:
  
  #scegli un giocatore casuale per la squadra A
  giocatoreA = choice(giocatori)
  teamA.append(giocatoreA)
  #rimuovi il giocatore scelto dalla lista dei giocatori
  giocatori.remove(giocatoreA)
  
  #interrompi il cliclo se non ci sono giocatori da estrarre
  if giocatori == []: 
    break
  
  #scegli un giocatore casuale per la squadra B
  giocatoreB = choice(giocatori)
  teamB.append(giocatoreB)
  #rimuovi il giocatore scelto dalla lista giocatori
  giocatori.remove(giocatoreB)

#scegli nomi di team casuali per i 2 team
teamNomeA = choice(teamNomi)
teamNomi.remove(teamNomeA)
teamNomeB = choice(teamNomi)
teamNomi.remove(teamNomeB)

#stampa i team
print('\nEcco le squadre:\n')
print(teamNomeA, teamA)
print(teamNomeB, teamB)