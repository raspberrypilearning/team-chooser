## Αρχεία

Μπορείς να χρησιμοποιήσεις ένα αρχείο για να αποθηκεύσεις τη λίστα των παικτών σου.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Πρόσθεσε πληκτρολογώντας τους παίκτες σου στο νέο αρχείο. Βεβαιώσου ότι δεν υπάρχει κενή γραμμή μετά τον τελευταίο παίκτη.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Άλλαξε στο πρόγραμμα τη λίστα παικτών `players` ώστε να είναι κενή.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Άνοιξε το αρχείο `players.txt` (το `'r'` σημαίνει μόνο για ανάγνωση).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Διάβασε τους παίκτες από το αρχείο και πρόσθεσέ τους στη λίστα `players`. (Ο κώδικας `splitlines` σημαίνει ότι κάθε γραμμή του αρχείου είναι ένα νέο στοιχείο στη λίστα `players`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Εάν δοκιμάσεις τον κώδικα, θα πρέπει να λειτουργεί ακριβώς όπως και πριν. Ωστόσο, τώρα είναι πολύ πιο εύκολο να προσθέσεις παίκτες στο αρχείο `players.txt`.

\--- /task \---