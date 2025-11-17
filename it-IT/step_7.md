## File

Puoi usare un file per memorizzare la tua lista di giocatori.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Aggiungi i tuoi giocatori al tuo nuovo file. Assicurati che non ci sia una riga vuota dopo il tuo ultimo giocatore.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Cambia la tua lista `giocatori` in modo che sia vuota.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Apri il tuo file `giocatori.txt ` (la lettera `'r'` significa in sola lettura).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Leggi la lista dal file e aggiungila alla tua lista `giocatori`. (Il codice `splitlines` significa che ogni riga nel file deve essere trattata come un nuovo elemento da inserire nella lista `giocatori`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Se provi il tuo codice, dovrebbe funzionare esattamente come in precedenza. Tuttavia, ora è molto più semplice aggiungere giocatori al tuo file `giocatori.txt `.

\--- /task \---