#!/bin/python3

from random import choice

# créer une liste de joueurs à partir d'un fichier
joueurs = []
file = open('joueurs.txt', 'r')
joueurs = file.read().splitlines()
print('Joueurs:', joueur)

#créer une liste de noms d'équipe à partir d'un fichier
Nomsequipe = []
file = open('Nomsequipe.txt', 'r')
Nomsequipe = file.read().splitlines()
print('Noms d'équipe:', Nomsequipe)

#créer des listes d'équipe vides
equipeA = []
equipeB = []

#boucler jusqu'à ce qu'il n'y ait plus de joueurs restants
while len(joueurs) > 0:
  
  #choisir un joueur aléatoire pour l'équipe A
  joueurA = choice(joueurs)
  equipeA.append(joueurA)
  #supprimer le joueur de la liste des joueurs
  joueurs.remove(joueurA)
  
  #sortir de la boucle s'il n'y a plus de joueurs restants
  if joueurs == []: 
    break
  
  #choisir un joueur aléatoire pour l'équipe B
  equipeB = choice(joueurs)
  equipeB.append(equipeB)
  #supprimer le joueur de la liste des joueurs
  joueurs.remove(joueurB)

#choisir un nom d'équipe aléatoire pour les 2 équipes
NomequipeeA = choice(Nomsequipe)
Nomsequipe.remove(NomequipeA)
NomequipeB = choice(Nomsequipe)
Nomsequipe.remove(NomequipeB)

#afficher les équipes
print('\nVoici tes équipes:\n')
print(NomequipeA, equipeA)
print(NomequipeB, equipeB)