#!/bin/python3

from random import choice

#Erstelle eine Liste von Spielern aus einer Datei
spieler = []
datei = open('spieler.txt', 'r')
spieler = datei.read().splitlines()
print('Spieler: ', spieler)

#Erstelle eine Liste von Teamnamen aus einer Datei
teamNamen = []
datei = open('teamNamen.txt', 'r')
teamNamen = datei.read().splitlines()
print ('Teamnamen: ', teamNamen)

#leere Teamlisten erstellen
teamA = []
teamB = []

#mache eine Schleife bis keine Spieler mehr übrig sind
while len(spieler) > 0:
  
  #Wähle einen zufälligen Spieler für Team A
  spielerA = choice(spieler)
  teamA.append(spielerA)
  #den Spieler aus der Spielerliste entfernen
  spieler.remove(spielerA)
  
  #brich die Schleife ab, wenn keine Spieler mehr vorhanden sind
  if players == []: 
    break
  
  #Wähle einen zufälligen Spieler für Team B
  spielerB = choice(spieler)
  teamB.append(spielerB)
  #den Spieler aus der Spielerliste entfernen
  spieler.remove(spielerB)

#Wähle zufällige Teamnamen für die 2 Teams
teamNameA = choice(teamNamen)
teamNamen.remove(teamNameA)
teamNameB = choice(teamNamen)
teamNamen.remove(teamNameB)

#gib die Teams aus
print('\nHier sind deine Teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)