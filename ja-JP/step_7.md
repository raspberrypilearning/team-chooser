## ファイル

ファイルを使用して、選手のリストを保存することができます。

--- task ---

**Add file** をクリックし、 `players.txt`という新しいファイルを作成します。

![プロジェクトファイルメニューの下に表示されるファイル追加ボタン](images/Add_file.png)

--- /task ---

--- task ---

+ 新しいファイルにプレーヤーを追加します。 最後のプレーヤーの後に空白行がないことを確認してください。

![players.txt 内の名前を示すスクリーンショット](images/players_file.png)

--- /task ---

--- task ---

`人のプレイヤー` リストを空になるように変更します。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from random import choice

players = []

team_A = []
team_B = []

--- /code ---

--- /task ---

--- task ---

`players.txt` ファイルを開きます（ `'r'` は読み取り専用です）。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4
---
from random import choice

players = []
file = open('players.txt', 'r')

team_A = []
team_B = []

--- /code ---

--- /task ---

--- task ---

ファイルからリストを読み、 `人のプレイヤーに` リストを追加します。 （ `スプリットライン` コードは、ファイル内のすべての行が `人のプレイヤー` リストの新しいアイテムであることを意味します）。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

team_A = []
team_B = []

--- /code ---

--- /task ---

--- task ---

あなたのコードをテストするならば、前とまったく同じように動作するはずです。 ただし、 `players.txt` ファイルにプレーヤーを追加する方がはるかに簡単です。

--- /task ---