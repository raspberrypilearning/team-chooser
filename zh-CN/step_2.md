## 队员

让我们首先创建一个可供选择的队员列表。

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

您可以使用变量来保存队员**列表**

列表应在一对方括号`[ ]`中 ，列表中的成员之间用逗号分隔。

首先在你的程序中添加一个队员列表。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

添加此代码以显示`players`变量：

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

您可以通过在变量名称后面的方括号中添加其位置来获取列表中的一个成员。

列表中的第一个成员在**位置０**。 这与Scratch不同，后者是从1开始。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---