## Dateien

Du kannst eine Datei verwenden, um deine Spielerliste zu speichern.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Füge deine Spieler deiner neuen Datei hinzu. Stelle sicher, dass sich nach deinem letzten Spieler keine Leerzeile befindet.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Ändere deine Liste `spieler`, so dass sie leer ist.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Öffne deine Datei `spieler.txt` (das `'r'` bedeutet schreibgeschützt).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Lese die Liste aus der Datei und füge sie der Liste `spieler` hinzu. (Der Code `splitlines` bedeutet, dass jede Zeile in der Datei ein neues Element in der Liste `spieler` ist).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Wenn du deinen Code testest, sollte er genauso funktionieren wie zuvor. Es ist nun jedoch viel einfacher, Spieler zu der Datei `spieler.txt` hinzuzufügen.

\--- /task \---