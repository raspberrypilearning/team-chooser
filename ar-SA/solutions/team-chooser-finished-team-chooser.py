#!/bin/python3

from random import choice

#إنشاء قائمة لاعبين من ملف
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('اللاعبين:', players)

#إنشاء قائمة باسماء الفرق من ملف
teamNames = []
file = open ('teamNames.txt'، 'r')
teamNames = file.read().splitlines()
print('أسماء الفريق:', teamNames)

# إنشاء قوائم فريق فارغة
teamA = []
teamB = []

#كرر حتى لايتبقى لاعبين
while len(players) > 0:
  
  #اختر لاعب عشوائي للفريق A
  playerA = choice(players)
  teamA.append(playerA)
  #إزالة اللاعب من قائمة اللاعبين
  players.remove(playerA)
  
  #الخروج من الحلقة إذا لم يتبقى لاعبين
  if players == []: 
    break
  
  #اختار لاعب عشوائي للفريق B
  playerB = choice(players)
  teamB.append(playerB)
  #إزالة اللاعب من قائمة اللاعبين
  players.remove(playerB)

#اختر أسماء فرق عشوائية للفريقين
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

# اطبع الفرق
print('\nهذه الفرق الخاصه بك:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)