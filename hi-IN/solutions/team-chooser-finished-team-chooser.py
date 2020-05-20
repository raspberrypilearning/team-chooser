#!/bin/python3

यादृच्छिक आयात विकल्प से

#फ़ाइल से खिलाड़ियों की एक सूची बनाएं
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

#फ़ाइल से खिलाड़ियों की एक सूची बनाएं
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)

#टीम की खाली सूचियां बनाएं
teamA = []
teamB = []

#लूप चलाएँ जब तक कोई खिलाड़ी नहीं बचे हैं
while len(players) > 0:
  
  # ए टीम के लिए एक यादृच्छिक खिलाड़ी चुनें
  playerA = choice(players)
  teamA.append(playerA)
  # खिलाड़ियों की सूची से खिलाड़ी को निकालें
  players.remove(playerA)
  
  #यदि कोई खिलाड़ी नहीं बचा है तो लूप ब्रेक करे
  if players == []: 
    break
  
  #टीम बी के लिए एक यादृच्छिक खिलाड़ी चुनें
  playerB = choice(players)
  teamB.append(playerB)
  # खिलाड़ियों की सूची से खिलाड़ी को निकालें
  players.remove(playerB)

#2 टीमों के लिए यादृच्छिक टीम के नाम चुनें
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#टीमों को प्रिंट करें
print('\nHere are your teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)