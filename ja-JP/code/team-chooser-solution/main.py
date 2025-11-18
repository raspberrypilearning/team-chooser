from random import choice

# ファイルからプレイヤーの一覧を作る
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

# ファイルからチーム名一覧を作る
team_names = []
file = open('team_names.txt', 'r')
team_names = file.read().splitlines()

# 空のチーム一覧をつくる
team_A = []
team_B = []

# プレイヤーが無くなるまでループする
while len(players) > 0:
  
    # チームAのプレイヤーをランダムに選ぶ
    player_A = choice(players)
    team_A.append(player_A)
    # プレイヤーをプレイヤー一覧から削除する
    players.remove(player_A)
  
    # プレイヤーが残っていない場合はループを抜ける
    if players == []: 
        break
  
    # チームBのプレイヤーをランダムに選ぶ
    player_B = choice(players)
    team_B.append(player_B)
    # プレイヤーをプレイヤー一覧から削除する
    players.remove(player_B)

# ランダムなチーム名を2チーム分選ぶ
team_name_A = choice(team_names)
team_names.remove(team_name_A)
team_name_B = choice(team_names)
team_names.remove(team_name_B)

# チームを出力する
print('\nあなたのチーム:\n")
print(team_name_A, team_A)
print(team_name_B, team_B)