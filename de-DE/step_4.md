## Zufällig ausgesuchte Mitspieler

Lass uns Spieler zufällig auswählen!

\--- task \---

Um einen zufälligen Spieler von deiner Liste `spieler` zu bekommen, musst du zuerst den Teil `choice` des Moduls `random` importieren.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Um einen zufälligen Spieler zu erhalten, kannst du die Option `choice` verwenden. (Du kannst den Code zum Ausgeben für aller Spieler auch löschen, um einzelne Spieler auszugeben.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Teste deinen `choice` Code ein paar Mal und es sollte jedes Mal eine anderer Spieler ausgewählt werden.

\--- /task \---

\--- task \---

Du kannst auch eine neue Variable mit dem Namen `spielerA` erstellen und sie dann zum Speichern deines zufälligen Spielers zu verwenden.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Du benötigst eine neue Liste, um alle Spieler in Team A zu speichern. Zunächst sollte diese Liste leer sein.

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

Du kannst jetzt deinen zufällig ausgewählten Spieler zu `teamA` hinzufügen. Dazu kannst du `teamA.append` verwenden (**append** bedeutet am Ende hinzufügen).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Nachdem ein Spieler ausgewählt wurde, kannst du ihn aus der Liste `spieler` entfernen.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Teste diesen Code, indem du eine Ausgabe mit `print` hinzufügst, um die noch auswählbaren Elemente der Liste `spieler` anzuzeigen.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---