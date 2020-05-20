#!/bin/python3

from random import choice

# 파일에서 플레이어 리스트 불러오기
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('플레이어 목록:', players)

# 파일에서 불러온 플레이어 리스트 List에 삽입
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('팀 목록:', teamNames)

# 빈 팀 List 만들기
teamA = []
teamB = []

# 남은 플레이어가 없을 때까지 반복
while len(players) > 0:
  
  # 팀 A의 임의의 플레이어 선택
  playerA = choice(players)
  teamA.append(playerA)
  # 선택된 플레이어를 플레이어 리스트에서 제거
  players.remove(playerA)
  
  # 만약 플레이어가 리스트에 없다면, 루프에서 벗어납니다.
  if players == []: 
    break
  
  # 팀 B의 임의의 플레이어 선택
  playerB = choice(players)
  teamB.append(playerB)
  # 선택된 플레이어를 플레이어 리스트에서 제거
  players.remove(playerB)

# 두 팀에 임의의 팀 이름 부여
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)

# 팀 배정 결과 출력
print('팀 배정 결과:')
print(teamNameA, teamA)
print(teamNameB, teamB)