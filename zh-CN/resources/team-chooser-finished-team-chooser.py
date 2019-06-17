#!/bin/python3

from random import randint

#从文件中导入队员名单
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('队员：', players)

#从文件中导入团队名单
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('队名：', teamNames)

#创建空的团队人员名单
teamA = []
teamB = []

#重复循环直到所有队员全部被选走
while len(players) > 0:
  
  #为A队随机选择一名队员
  playerA = choice(players)
  teamA.append(playerA)
  #将已选的队员从队员名单中去除
  players.remove(playerA)
  
  #如果没有队员剩下了，则跳出循环
  if players == []: 
    break
  
  #为B队随机选择一名队员
  playerB = choice(players)
  teamB.append(playerB)
  #将已选的队员从队员名单中去除
  players.remove(playerB)

#为两队随机选择队名
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

#显示队名
print('\n这是你的团队：\n')
print(teamNameA, teamA)
print(teamNameB, teamB)