## Fichiers

Tu peux utiliser une variable pour stocker une liste de joueurs.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Ajoute tes joueurs à ton nouveau fichier. Assure-toi qu'il n'y a pas de ligne blanche après ton dernier joueur.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Change ta liste `joueurs` afin qu'elle soit vide.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Ouvre ton ficher `joueur.txt ` (le `'r'` signifie en lecture seule).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Lire la liste à partir du fichier et ajouter à ta liste `joueurs`. (Le code `splitlines` signifie que chaque ligne dans le fichier est un nouvel élément dans la liste `joueurs` ).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Si tu testes ton code, il devrait fonctionner exactement comme avant. Cependant, il est maintenant beaucoup plus facile d'ajouter des joueurs à ton fichier `joueurs.txt`.

\--- /task \---