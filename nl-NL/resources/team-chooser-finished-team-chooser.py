#!/bin/python3

from random import choice

#maak een lijst van spelers vanuit een bestand
spelers = []
file = open('spelers.txt', 'r')
spelers = file.read().splitlines()
print('Spelers:', spelers)

#maak een lijst van teamnamen vanuit een bestand
teamNamen = []
file = open('teamnamen.txt', 'r')
teamNamen = file.read().splitlines()
print('Teamnamen:', teamNamen)

#maak lege teamlijsten
teamA = []
teamB = []

#herhaal in een lus/loop tot er geen spelers meer over zijn
while len(spelers) > 0:
  
  #kies een willekeurige speler voor team A
  spelerA = choice(spelers)
  teamA.append(spelerA)
  #verwijder de speler van de spelerslijst
  spelers.remove(spelerA)
  
  #ga uit deze loop als er geen spelers meer over zijn
  if spelers == []: 
    break
  
  #kies een willekeurige speler voor team B
  spelerB = choice(spelers)
  teamB.append(spelerB)
  #verwijder de speler van de spelerslijst
  spelers.remove(spelerB)

#kies willekeurig namen voor de twee teams
teamNaamA = choice(teamNamen)
teamNamen.remove(teamNaamA)
teamNaamB = choice(teamNamen)
teamNamen.remove(teamNaamB)

#print de teams
print('\nHier zijn je teams:\n')
print(teamNaamA, teamA)
print(teamNaamB, teamB)