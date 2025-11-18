## たくさんの選手を選ぶ

次に、すべてのプレイヤーがチームに選ばれたことを確認する必要があります。

--- task ---

チームAとチームBのためにプレイヤーを選ぶコードを選択し、Tabキーを押してコードをインデントします。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 10-20
---
from random import choice

players = ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']
print(players)

team_A = []
team_B = []

    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('残りプレイヤー数: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('残りプレイヤー数: ', players)
    

--- /code ---

--- /task ---

--- task ---

`players`リストが空になるまでプレイヤーを選び続けるために**while**ループを追加します。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 9
---
while len(players) > 0:
    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('残りのプレイヤー数: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('残りプレイヤー数: ', players)
    

--- /code ---

--- /task ---

--- task ---

コードを実行してテストします。 残りのプレイヤーがいなくなるまでチームAとチームBにプレイヤーが選ばれるのが見られるはずです。

```
    ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']
    ハーマイオニー
    残りプレイヤー: ['ハリー', 'ネビル', 'ジニー']
    ハリー
    残りプレイヤー: ['ネビル', 'ジニー']
    ジニー
    残りプレイヤー: ['ネビル']
    ネビル
    残りプレイヤー: []
```

--- /task ---

--- task ---

`team_A`のリストを出力するためのコードを`while`ループの**後ろ**に追加します(インデントしないでください)。

これはすべてのプレイヤーが選ばれた後一度だけ`team_A`を出力することを意味します。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 22
---
while len(players) > 0:
    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('残りのプレイヤー数: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('残りプレイヤー数: ', players)
    

print('チームA', team_A)

--- /code ---

--- /task ---

--- task ---

`team_B`でも同じことができますし、他の出力コードを削除することもできます。これらはあなたのコードをテストするためだけに使われているからです。

コードの外観は次のとおりです。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from random import choice

players = ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']

team_A = []
team_B = []

while len(players) > 0:
    player_A = choice(players)
    team_A.append(player_A)
    players.remove(player_A)
    
    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)

print('チームA', team_A)
print('チームB', team_B)

--- /code ---

--- /task ---

--- task ---

あなたのコードをもう一度試してみると、あなたのプレイヤーリストと最終的なチームが表示されます。

```
    チームA ['ハーマイオニー', 'ハリー']
    チームB ['ネビル', 'ジニー']
```

--- /task ---