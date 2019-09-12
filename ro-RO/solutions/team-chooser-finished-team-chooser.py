#!/bin/python3

from random import choice

#creeaza o lista de jucatori dintr-un fisier
jucatori = []
fisier = open('jucatori.txt', 'r')
jucatori = fisier.read().splitlines()
print('Jucatori:', jucatori)

#creeaza o lista de nume pentru echipe dintr-un fisier
numeEchipe = []
fisier = open('numeEchipe.txt', 'r')
numeEchipe = fisier.read().splitlines()
print('Nume pentru echipe:', numeEchipe)

#creeaza liste goale pentru echipe
echipaA = []
echipaB = []

#repeta pana cand nu mai ramane niciun jucator
while len(jucatori) > 0:
  
  #alege un jucator aleatoriu pentru echipa A
  jucatorA = choice(jucatori)
  echipaA.append(jucatorA)
  #scoate jucatorul din lista jucatori
  jucatori.remove(jucatorA)
  
  #iesi din bucla daca nu mai este niciun jucator
  if jucatori == []: 
    break
  
  #alege un jucator aleatoriu pentru echipa B
  jucatorB = choice(jucatori)
  echipaB.append(jucatorB)
  #scoate jucatorul din lista jucatori
  jucatori.remove(jucatorB)

#alege nume de echipe la intamplare pentru cele doua echipe
numeEchipaA = choice(numeEchipe)
numeEchipe.remove(numeEchipaA)
numeEchipaB = choice(numeEchipe)
numeEchipe.remove(numeEchipaB)

#afiseaza echipele
print('\nAcestea sunt echipele tale:\n')
print(numeEchipaA, echipaA)
print(numeEchipaB, echipaB)