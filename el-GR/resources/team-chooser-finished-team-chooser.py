#!/bin/python3

from random import choice

#δημιούργησε μια λίστα παικτών από ένα αρχείο
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Παίκτες:', players)

#δημιούργησε μια λίστα ονομάτων ομάδων από ένα αρχείο
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Ονομασίες ομάδων:', teamNames)

#δημιούργησε κενές λίστες ομάδων
teamA = []
teamB = []

#επανάλαβε μέχρις ότου δεν έχουν μείνει παίκτες
while len(players) > 0:
  
  #επέλεξε έναν τυχαίο παίκτη για την ομάδα Α
  playerA = choice(players)
  teamA.append(playerA)
  #αφαίρεσε τον παίκτη από τη λίστα παικτών
  players.remove(playerA)
  
  #σταμάτα την επανάληψη αν δεν έχουν μείνει παίκτες
  if players == []: 
    break
  
  #επέλεξε έναν τυχαίο παίκτη για την ομάδα Β
  playerB = choice(players)
  teamB.append(playerB)
  #αφαίρεσε τον παίκτη από τη λίστα παικτών
  players.remove(playerB)

#επέλεξε τυχαία ονόματα για τις 2 ομάδες
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#εμφάνισε τις ομάδες
print('\nΑυτές είναι οι ομάδες:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)