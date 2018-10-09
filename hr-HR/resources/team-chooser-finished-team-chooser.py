#!/bin/python3

from random import choice

#stvaranje popisa igrača iz datoteke
igraci = []
file = open('igraci.txt', 'r')
igraci = file.read().splitlines()
print('Igrači:', igraci)

#stvaranje popisa imena timova iz datoteke
imenaTimova = []
file = open('imenaTimova.txt', 'r')
imenaTimova = file.read().splitlines()
print('Imena timova:', imenaTimova)

#stvaranje prazne liste timova
timA = []
timB = []

#ponavljaj dok ne ostane nijedan igrač
while len(igraci) > 0:
  
  #odabir nasumičnog igrača za tim A
  igracA= choice(igraci)
  timA.append(igracA)
  #uklanjanje igrača s popisa igrača
  igraci.remove(igracA)
  
  #zaustavljanje petlje ako nema više igrača
  if igraci == []: 
    break
  
  #odabir nasumičnog igrača za tim B
  igracB = choice(igraci)
  timB.append(igracB)
  #uklanjanje igrača s popisa igrača
  igraci.remove(igracB)

#odabir nasumičnih imena timova
imeTimaA = choice(imenaTimova)
imenaTimova.remove(imeTimaA)
imeTimaB = choice(imenaTimova)
imenaTimova.remove(imeTimaB)

#ispisivanje timova
print('\nOvo su tvoji timovi:\n')
print(imeTimaA, timA)
print(imeTimaB, timB)