#!/bin/python3

from random import choice

#kreiraj listu igrača iz datoteke
igraci = []
datoteka = open('igraci.txt', 'r')
igraci = datoteka.read().splitlines()
print('Igrači:', igraci)

#kreiraj listu naziva timova iz datoteke
naziviTimova = []
datoteka = open('naziviTimova.txt', 'r')
naziviTimova = datoteka.read().splitlines()
print('Nazivi timova:', naziviTimova)

#kreiraj prazne liste timova
timA = []
timB = []

#ponavljaj dok više ne bude igrača
while len(igraci) > 0:
  
  #odaberi nasumičnog igrača za tim A
  igracA = choice(igraci)
  timA.append(igracA)
  #ukloni igrača sa liste igrača
  igraci.remove(igracA)
  
  #zaustavi petlju ako više nema igrača
  if igraci == []: 
    break
  
  #odaberi nasumičnog igrača za tim B
  igracB = choice(igraci)
  timB.append(igracB)
  #ukloni igrača sa liste igrača
  igraci.remove(igracB)

#odaberi nasumične nazive za 2 tima
nazivTimaA = choice(naziviTimova)
naziviTimova.remove(nazivTimaA)
nazivTimaB = choice(naziviTimova)
naziviTimova.remove(nazivTimaB)

#ispiši timove
print('\nOvo su tvoji timovi:\n')
print(nazivTimaA, timA)
print(nazivTimaB, timB)