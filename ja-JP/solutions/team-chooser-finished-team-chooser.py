#!/bin/python3

from random import choice

# ファイルからプレイヤーの一覧を作る
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('プレイヤーたち:', players)

# ファイルからチーム名一覧を作る
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('チーム名たち:', teamNames)

# 空のチーム一覧をつくる
teamA = []
teamB = []

# プレイヤーが無くなるまでループする
while len(players) > 0:
  
  # チームAのプレイヤーをランダムに選ぶ
  playerA = choice(players)
  teamA.append(playerA)
  # プレイヤーをプレイヤー一覧から削除する
  players.remove(playerA)
  
  # プレイヤーが残っていない場合はループを抜ける
  if players == []: 
    break
  
  # チームBのプレイヤーをランダムに選ぶ
  playerB = choice(players)
  teamB.append(playerB)
  # プレイヤーをプレイヤー一覧から削除する
  players.remove(playerB)

# ランダムなチーム名を2チーム分選ぶ
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

# チームを出力する
print('\nあなたのチーム:\n")
print(teamNameA, teamA)
print(teamNameB, teamB)