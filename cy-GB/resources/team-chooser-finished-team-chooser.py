#!/bin/python3

from random import choice

#crëwch restr o chwaraewyr o ffeil
chwaraewyr = []
ffeil = open('chwaraewyr.txt', 'r')
chwaraewyr = ffeil.read().splitlines()
print('Chwaraewyr:', chwaraewyr)

#crëwch restr o enwau tîm o ffeil
Enwautim = []
ffeil = open('Enwautim.txt', 'r')
Enwautim = ffeil.read().splitlines()
print('Enwau tîm:', Enwautim)

#crëwch restrau tîm gwag
timA = []
timB = []

#dolen hyd nad oes unrhyw chwaraewyr ar ôl
while len(chwaraewyr) > 0:
  
  #dewiswch chwaraewr ar hap i’r tîm A
  chwaraewyrA = choice(chwaraewyr)
  timA.append(chwaraewyrA)
  #tynnwch y chwaraewyr o restr y chwaraewyr
  chwaraewyr.remove(chwaraewyrA)
  
  #torrwch allan o’r ddolen os nad oes unrhyw chwaraewyr ar ôl
  if chwaraewyr == []: 
    break
  
  #dewiswch chwaraewyr ar hap i dîm B
  chwaraewyrB = choice(chwaraewyr)
  timB.append(chwaraewyrB)
  #tynnwch y chwaraewr o restr y chwaraewyr
  chwaraewyr.remove(chwaraewyrB)

#dewiswch enwau tîm ar hap i’r 2 dîm
EnwtimA = choice(Enwautim)
Enwautim.remove(EnwtimA)
EnwtimB = choice(Enwautim)
Enwautim.remove(EnwtimB)

#printiwch y timau
print('\nDyma eich timau:\n')
print(EnwtimA, timA)
print(EnwtimB, timB)