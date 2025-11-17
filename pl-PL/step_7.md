## Pliki

Do przechowywania listy graczy możesz użyć pliku.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Dodaj swoich graczy do tego pliku. Upewnij się, że po twoim ostatnim graczu nie ma pustej linii.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Zmień listę `gracze` tak, aby była pusta.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Otwórz plik `gracze.txt` (`'r'` oznacza tylko do odczytu, ang. read-only).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Odczytaj listę z pliku i dodaj do listy `gracze`. (Funkcja `splitlines` oznacza, że ​​każda linia w pliku jest nową pozycją na liście `gracze`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Kiedy przetestujesz swój kod, powinien on działać dokładnie tak samo jak poprzednio. Teraz jednak znacznie łatwiej jest dodać graczy do twojego pliku `gracze.txt`.

\--- /task \---