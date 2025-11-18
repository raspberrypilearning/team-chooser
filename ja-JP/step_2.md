## プレイヤー

まず選ぶプレイヤーのリストを作成しましょう。

--- task ---

[アーチェリースターター](https://editor.raspberrypi.org/ja-JP/projects/team-chooser-starter){:target="_blank"}プロジェクトを開く。 Code Editorは別のブラウザタブで開きます。

--- /task ---

--- task ---

プレイヤーの**リスト**を保存しておくのに変数を使うことができます。

リストは角括弧 `[ ]`で、リスト内の各項目の間にコンマを入れてください。

あなたのプログラムにプレイヤーのリストを追加することから始めます。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
players = ['ハリー', 'ハーマイオニー']

--- /code ---

--- /task ---

--- task ---

`players`変数を出力するのに以下のコードを書き足します:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
players = ['ハリー', 'ハーマイオニー']
print(players)

--- /code ---

--- /task ---

--- task ---

リストの要素を取得するには、変数名の後ろの角括弧の中に位置を付けます。

リストの最初の項目は **位置0**です。 これは位置が1から始まるScratchとは異なります。

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4-5
---
players = ['ハリー', 'ハーマイオニー']
print(players)

print(players[0])
print(players[1])

--- /code ---

--- /task ---