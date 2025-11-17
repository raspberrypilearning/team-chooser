## 隨機隊員

讓我們隨機選擇一些隊員！

\--- task \---

為了能夠從你的`players`列表中獲得一個隨機隊員，首先你需要匯入`random`模組中的`choice` 函式。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

要獲得一個隨機的隊員, 你可以使用 `choice`。 （您也可以刪除程式碼以顯示單個隊員。）

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

測試幾次你的 `choice` 程式碼, 你會看到每次都有一個不同的隊員被選中。

\--- /task \---

\--- task \---

您還可以建立一個名為` playerA `的新變數, 並使用它來儲存你隨機選擇的隊員。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

你還需要一個新的列表來儲存Ａ隊中的所有隊員。在一開始，這個列表應該是空的。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

team_A = []

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

現在你可以將隨機選擇的隊員新增到`teamA`。 為此，你可以使用` teamA.append` （**append** 表示在後方新增）。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

現在你可以將被選中的隊員從 `players` 列表中刪除。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

通過新增` print` 指令來測試此程式碼, 以顯示` players`列表中剩下可以選取的隊員。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---