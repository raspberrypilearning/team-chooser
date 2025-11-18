## 奇妙な選手

奇数のプレイヤーと作業するようプログラムを改善してみましょう。

--- task ---

+ プレイヤー数が奇数になるように、 `players.txt` リストに別の名前を追加します。

--- code ---
---
language: python
filename: players.txt
line_numbers: true
line_number_start: 1
line_highlights: 5
---
ハリー
ハーマイオニー
ネビル
ジニー
ルーナ

--- /code ---

--- /task ---

--- task ---

コードをテストすると、エラーメッセージが表示されます。

![スクリーンショット](images/error.png)

--- /task ---

このエラーは、あなたのプログラムがAチームとBチームのランダムプレイヤーを選択し続けるためです。しかし、奇数のプレーヤーがある場合、Aチームのプレーヤーを選んだ後、Bチームの選手はいません。

--- task ---

このバグを修正するには、にあなたのプログラムを伝えることができます `ブレーク` あなたのうち `中` お使いの場合はループ `選手` リストは空です。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 15-16
---
while len(players) > 0:
    player_A = choice(players)
    team_A.append(player_A)
    players.remove(player_A)

    if players == []:
        break
    
    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)

--- /code ---

--- /task ---

--- task ---

コードを再度テストすると、奇数のプレイヤーで動作することがわかります。

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
チームA ['ハリー', 'ジニー', 'ルーナ']
チームB ['ハーマイオニー', 'ネビル']

--- /code ---

--- /task ---