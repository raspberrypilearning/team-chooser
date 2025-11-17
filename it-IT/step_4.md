## Giocatori casuali

Scegliamo giocatori casuali!

\--- task \---

Per essere in grado di ottenere un giocatore casuale dalla tua lista di `giocatori`, per prima cosa devi importare il metodo `choice` contenuto nel modulo `random`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Per ottenere un giocatore casuale, puoi usare `choice`. (Puoi anche cancellare il codice per stampare i singoli giocatori.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Metti alla prova il tuo codice `choice` alcune volte e dovresti verificare che ogni volta viene scelto un giocatore diverso.

\--- /task \---

\--- task \---

Puoi anche creare una nuova variabile chiamata `playerA` e usarla per memorizzare il tuo giocatore casuale.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Avrai bisogno di una nuova lista per archiviare tutti i giocatori della squadra A. Per cominciare, questa lista deve essere vuota.

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

Ora puoi aggiungere il tuo giocatore scelto a caso al `teamA`. Per fare ciò, puoi usare `teamA.append` (**append** significa aggiungere alla fine).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Ora che il tuo giocatore è stato scelto, puoi rimuoverlo dalla tua lista di `giocatori`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Prova questo codice aggiungendo un comando `print`, per mostrare i `giocatori` rimasti da scegliere.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---