## 随机队员

让我们随机选择一些队员！

\--- task \---

为了能够从你的 `队员` 列表中获得一个随机队员，首先你需要导入`random`模块中的`choice` 函数。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

要获得一个随机的队员, 你可以使用 `choice`。 （您也可以删除代码以显示单个队员。）

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

测试几次你的 `choice` 代码, 你应该看到每次都会有一个不同的队员被选中。

\--- /task \---

\--- task \---

您还可以创建一个名为 `playerA` 的新变量, 并使用它来保存随机选择的队员。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

你还需要一个新的列表来保存Ａ队中的所有队员。在一开始，这个列表应该是空的。

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

现在你可以将随机选择的队员添加到`teamA`。 为此，你可以使用 `teamA.append` 方法（**append** 表示添加到末尾）。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

现在, 你的队员已被选中，你可以将他们移出 `players` 列表。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

通过添加 `print` 命令来测试此代码, 以显示 `players`列表中余下的可供选择的队员。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---