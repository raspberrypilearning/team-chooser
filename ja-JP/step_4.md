## ランダムなプレイヤー

ランダムにプレイヤーを選んでみましょう！

--- task ---

`players`リストからランダムにプレイヤーを得るには、まず`random`モジュールのうちの `choice` をインポートする必要があります。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
from random import choice

players = ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']
print(players)

print(players[0])
print(players[1])

--- /code ---

--- /task ---

--- task ---

ランダムにプレイヤーを取得するには、`choice`を使用します。 (個々のプレイヤーを出力するコードを削除することもできます)

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from random import choice

players = ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']
print(players)

print(choice(players))

--- /code ---

--- /task ---

--- task ---

`choice`コードを何度かテストし、毎回異なるプレーヤーが選択されるのを確認してみましょう。

--- /task ---

--- task ---

ランダムなプレイヤーを保存するために`player_A`という名前の変数を作りましょう。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
from random import choice

players = ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']
print(players)

player_A = choice(players)
print(player_A)

--- /code ---

--- /task ---

--- task ---

チームAのすべてのプレイヤーを保存するために新しいリストが必要です。このリストは空である必要があります。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from random import choice

players = ['ハリー', 'ハーマイオニー', 'ネビル', 'ジニー']
print(players)

team_A = []

player_A = choice(players)
print(player_A)

--- /code ---

--- /task ---

--- task ---

ランダムに選んだ選手を`team_A`に追加できます。 これを行うには、 `team_A.append`(**append**は末尾に追加することを意味します)を使用できます。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 10
---
player_A = choice(players)
print(player_A)
team_A.append(player_A)

--- /code ---

--- /task ---

--- task ---

選手たちを選び終えたので、 `players`リストからプレイヤーたちを削除できます。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 11
---
player_A = choice(players)
print(player_A)
team_A.append(player_A)
players.remove(player_A)

--- /code ---

--- /task ---

--- task ---

このコードをテストするには、 `print` コマンドを追加して、選んだ `players` を表示します。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 12
---
player_A = choice(players)
print(player_A)
team_A.append(player_A)
players.remove(player_A)
print('残りプレイヤー数: ', players)

--- /code ---

--- /task ---