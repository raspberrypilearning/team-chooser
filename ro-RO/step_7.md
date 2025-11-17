## Fișiere

Poți folosi un fișier pentru a salva lista ta de jucători.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Adaugă jucătorii tăi la noul tău fișier. Asigură-te că nu există nicio linie goală după ultimul tău jucător.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Golește lista ta de `jucatori`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Deschide fișierul tău `jucatori.txt` (`„r”` înseamnă read-only, adică numai citirile sunt permise).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Citește lista din fișier și adaug-o la lista ta de `jucatori`. (Codul `splitlines` înseamnă că fiecare linie din fișier reprezintă un element nou în lista `jucatori`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Dacă testezi codul, ar trebui să funcționeze la fel ca înainte. Cu toate acestea, acum este mult mai ușor să adaugi jucători la fișierul tău `jucatori.txt`.

\--- /task \---