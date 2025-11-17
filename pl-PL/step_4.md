## Losowi gracze

Wybierzmy losowych graczy!

\--- task \---

Aby wybrać losowego gracza z listy `gracze`, najpierw należy zaimportować `choice` z modułu `random`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Aby wybrać losowego gracza, możesz użyć `choice`. (Możesz również usunąć kod, który wypisuje poszczególnych graczy.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Przetestuj swój kod z funkcją `choice` kilka razy, a za każdym razem powinieneś zobaczyć innego gracza.

\--- /task \---

\--- task \---

Możesz też utworzyć nową zmienną o nazwie `graczA` i użyć jej do przechowywania wylosowanego gracza.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Będziesz potrzebować nowej listy do przechowywania wszystkich graczy w zespole A. Na początku ta lista powinna być pusta.

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

Możesz teraz dodać wylosowanego gracza do listy `zespolA`. Aby to zrobić, możesz użyć `zespolA.append` (**append** oznacza dodanie na koniec listy).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Po wybraniu gracza możesz usunąć go z listy `gracze`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Przetestuj ten kod, dodając polecenie `print`, aby pokazać, którzy `gracze` nie zostali jeszcze wylosowani.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---