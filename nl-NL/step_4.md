## Willekeurige spelers

We gaan spelers willekeurig kiezen

\--- task \---

Om ​​een willekeurige speler uit je `spelers` lijst te krijgen, moet je eerst het `choice` deel van de `random` module importeren.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Om een ​​willekeurige speler te krijgen, kun je `choice` gebruiken. (Je kunt ook de code verwijderen om individuele spelers te laten zien)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Test een paar keer de `choice` code en je ziet dat er elke keer een andere speler wordt gekozen.

\--- /task \---

\--- task \---

Je kunt ook een nieuwe variabele maken met de naam `spelerA` waar je de willekeurige speler in op kunt slaan.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Je hebt een nieuwe lijst nodig om alle spelers in team A op te slaan. Om te beginnen moet deze lijst leeg zijn.

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

Je kunt nu je willekeurig gekozen speler toevoegen aan `teamA`. Om dit te doen, kun je `teamA.append` gebruiken (**append** betekent aan het einde toevoegen).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Nu je speler is gekozen, kun je die verwijderen uit je lijst met `spelers`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Test de code door een `print` opdracht toe te voegen die de `spelers` laat zien die nog over zijn.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---