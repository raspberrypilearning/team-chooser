#!/bin/python3

من اختيار الاستيراد العشوائي

# إنشاء قائمة لاعبين من ملف
لاعبين = []
ملف = فتح('players.txt', 'r')
لاعبين =file.read().splitlines()
print ('اللاعبين:' ، اللاعبين)

# إنشاء قائمة لاعبين من ملف
أسماء المجموعه = []
file = open ('teamNames.txt'، 'r')
teamNames = file.read().splitlines()
print('أسماء الفريق:', teamNames)

# إنشاء قوائم فريق فارغة
teamA = []
teamB = []

#loop حتى لا يتم ترك أي لاعبين
بينما len (اللاعبين)> 0:
  
  #لختار لاعب عشوائي للفريق A
  playerA = الاختيار (اللاعبين)
  teamA.append (playerA)
  # إزالة اللاعب من قائمة اللاعبين
  players.remove (playerA)
  
  # الخروج من حلقة إذا لم يكن هناك لاعبين اليسار
  إذا كان اللاعبون == []: 
    استراحة
  
  #اختار لاعب عشوائي للفريق B
  playerB = الاختيار (اللاعبين)
  teamB.append (playerB)
  # إزالة اللاعب من قائمة اللاعبين
  players.remove (playerB)

#اختر أسماء الفرق بعشوائية للفريقين
teamNameA = choice (teamNames)
teamNames.remove (teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

# اطبع الفرق
print('\nهنا الفرق الخاصه بك:\n')
طباعة (teamNameA ، teamA)
طباعة (teamNameB ، teamB)