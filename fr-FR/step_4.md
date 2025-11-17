## Joueurs aléatoires

Choisissons des joueurs aléatoires!

\--- task \---

Pour pouvoir obtenir un joueur aléatoire parmi ta liste de ` joueurs`, tu devras d’abord importer le `choice` de la partie du module `random`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Pour obtenir un joueur aléatoire, tu peux utiliser `choice` . (Tu peux également supprimer le code pour imprimer des joueurs individuels.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Teste ton code `choice` plusieurs fois et tu devrais voir un joueur différent en étant choisi à chaque fois.

\--- /task \---

\--- task \---

Tu peux également créer une nouvelle variable appelée `joueurA` et l'utiliser pour stocker ton joueur aléatoire.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Tu auras besoin d'une nouvelle liste pour stocker tous les joueurs de l'équipe A. Pour commencer, cette liste devrait être vide.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

team_A = []

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Tu peux maintenant ajouter ton joueur aléatoire à l' `equipeA`. Pour ce faire, tu dois utiliser `equipeA.append` (**append** signifie ajouter à la fin).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Maintenant que ton joueur a été choisi, tu peux le supprimer de ta liste de `joueurs`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Teste ce code en ajoutant une commande `print`, pour afficher les `joueurs` restant à choisir.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---