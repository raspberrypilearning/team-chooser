## Ffeiliau

Gallwch ddefnyddio ffeil i storio eich rhestr o chwaraewyr.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Ychwanegu eich chwaraewyr at eich ffeil newydd. Gwnewch yn siŵr nad oes llinell wag ar ôl eich chwaraewr olaf.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Newid eich rhestr `chwaraewyr` fel ei bod yn wag.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Agorwch eich ffeil `chwaraewyr.txt` (mae `'r'` yn golygu darllen yn unig).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Darllenwch y rhestr o'r ffeil a'i hychwanegu at eich rhestr `chwaraewyr`. (Mae'r Cod `splitlines` (llinellau hollt) yn golygu bod pob llinell yn y ffeil yn eitem newydd yn y rhestr `chwaraewyr`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Os ydych chi'n profi eich cod, dylai weithio'n union yr un fath ag o'r blaen. Fodd bynnag, erbyn hyn mae'n llawer haws ychwanegu chwaraewyr at eich ffeil `chwaraewyr.txt`.

\--- /task \---