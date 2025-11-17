## 隊員

讓我們首先建立一個可供選擇的隊員列表。

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

您可以使用變數來儲存隊員**列表**

列表應在一對方括號`[ ]`中 ，列表中的成員之間用逗號分隔。

首先在你的程式中新增一個隊員列表。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

新增此程式碼以顯示`players`變數：

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

您可以透過在變數名稱後面的方括號中新增其位置來取得列表中的一個成員。

列表中的第一個成員在**位置０**。 這與Scratch不同，後者從位置1開始。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---