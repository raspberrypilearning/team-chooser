#!/bin/python3

from random import choice

#tworzenie listy graczy zapisanych w pliku
gracze = []
plik = open('gracze.txt', 'r')
gracze = plik.read().splitlines()
print('Gracze:', gracze)

#tworzenie listy nazw zespołów zapisanych w pliku
nazwyZespolow = []
plik = open('nazwyZespolow.txt', 'r')
nazwyZespolow = plik.read().splitlines()
print('Nazwy zespołów:', nazwyZespolow)

#tworzenie pustych list zawodników
zespolA = []
zespolB = []

#wykonywanie pętli tak długo, aż nie będzie więcej graczy
while len(gracze) > 0:
  
  #wybieranie losowego gracza do zespołu A
  graczA = choice(gracze)
  zespolA.append(graczA)
  #usuwanie gracza z listy graczy
  gracze.remove(graczA)
  
  #przerywanie pętli, jeśli nie ma więcej graczy
  if gracze == []: 
    break
  
  #wybieranie losowego gracza do zespołu B
  graczB = choice(gracze)
  zespolB.append(graczB)
  #usuwanie gracza z listy graczy
  gracze.remove(graczB)

#wybieranie losowej nazwy dla obu zespołów
nazwaZespoluA = choice(nazwyZespolow)
nazwyZespolow.remove(nazwaZespoluA)
nazwaZespoluB = choice(nazwyZespolow)
nazwyZespolow.remove(nazwaZespoluB)

#wyświetlanie zespołów
print('\nOto wylosowane zespoły:\n')
print(nazwaZespoluA, zespolA)
print(nazwaZespoluB, zespolB)