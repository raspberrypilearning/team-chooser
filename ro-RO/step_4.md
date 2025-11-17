## Jucători la întâmplare

Să alegem jucători la întâmplare!

\--- task \---

Pentru a putea obține un jucător aleatoriu din lista ta `jucatori`, întâi va trebui să imporți `choice` din modulul `random`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Pentru a obține un jucător aleatoriu, poți folosi `choice`. (Poți de asemenea să ștergi codul pentru a afișa jucători individuali.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Testează codul tău ce folosește `choice` de câteva ori și ar trebui să vezi un jucător diferit ales de fiecare dată.

\--- /task \---

\--- task \---

Poți de asemenea să creezi o nouă variabilă numită `jucatorA`, și să o folosești pentru a reține jucătorul tău aleatoriu.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Vei avea nevoie de o nouă listă pentru a reține toți jucătorii din echipa A. Pentru început, această listă trebuie să fie goală.

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

Acum poți adăuga jucătorul tău ales aleatoriu la `echipaA`. Pentru a face asta, poți folosi `echipaA.append` (**append** înseamnă adăugare la sfârșit).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Acum că jucătorul tău a fost ales, îl poți scoate din lista ta de `jucatori`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Testează acest cod prin adăugarea comenzii `print`, pentru a afișa `jucatorii` care au rămas de ales.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---