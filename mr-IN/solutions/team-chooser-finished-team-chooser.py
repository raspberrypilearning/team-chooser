#!/bin/python3

from random import choice

#फाइलमधून खेळाडूंची यादी तयार करा
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

#फाईलमधून टीमच्या नावांची यादी तयार करा
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)

#टीमच्या रिकाम्या याद्या तयार करा
teamA = []
teamB = []

#जोपर्यंत कोणतेही खेळाडू शिल्लक नाहीत तोपर्यंत लूप करा
while len(players) > 0:
  
  #team A साठी कोणताही खेळाडू निवडा
  playerA = choice(players)
  teamA.append(playerA)
  #players यादीतून खेळाडू काढून टाका
  players.remove(playerA)
  
  #कोणतेही खेळाडू शिल्लक नसल्यास लूपमधून बाहेर या
  if players == []: 
    break
  
  #team B साठी कोणताही खेळाडू निवडा
  playerB = choice(players)
  teamB.append(playerB)
  #players यादीतून खेळाडू काढून टाका
  players.remove(playerB)

#2 टीम्स साठी कोणते ही नावे निवडा
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#टीम्स प्रिंट करा
print('\nHere are your teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)