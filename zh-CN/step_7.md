## 文件

您可以使用文件来保存你的队员名单。

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ 将你的队员名单加入到新文件中。 确保在最后一名队员之后没有空行。

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

修改你的 `players` 列表, 清空。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

打开你的 `players.txt` 文件（`‘r‘` 表示只读打开）。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

从文件中读取列表并添加到`players`列表。 (`splitlines` 代码表示文件中的每一行都是 `players` 列表中的一个新成员)。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

如果进行测试，您的代码将与此前的运行一致。 然而，现在将队员添加到 `players.txt` 文件的做法要容易得多。

\--- /task \---