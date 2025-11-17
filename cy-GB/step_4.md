## Chwaraewyr ar hap

Gadewch i ni ddewis chwaraewyr ar hap!

\--- task \---

I allu cael chwaraewr ar hap o'ch rhestr `chwaraewyr`, yn gyntaf bydd angen i chi fewnosod y rhan `choice` (dewis) o'r modiwl `random` (ar hap).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

I gael chwaraewr ar hap, gallwch ddefnyddio `choice` (dewis). (Gallwch hefyd ddileu'r cod i argraffu chwaraewyr unigol.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Profwch eich cod `choice` (dewis) ychydig o weithiau a dylech weld chwaraewr gwahanol yn cael ei ddewis bob tro.

\--- /task \---

\--- task \---

Gallwch hefyd greu newidyn newydd o'r enw `chwaraewrA`, a'i ddefnyddio i storio eich chwaraewr ar hap.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Bydd angen rhestr newydd arnoch i storio pob un o'r chwaraewyr yn nhîm A. I ddechrau, dylai'r rhestr hon fod yn wag.

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

Nawr gallwch ychwanegu eich chwaraewr a ddewiswyd ar hap at `dîmA`. I wneud hyn, gallwch chi ddefnyddio `tîmA.append` (atodiad tîm A) mae (**atodiad** yn golygu ychwanegu at y diwedd).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Nawr mae eich chwaraewr wedi'i ddewis, gallwch ei dynnu oddi ar eich rhestr o `chwaraewyr`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Profwch y cod hwn trwy ychwanegu gorchymyn `print` (argraffu), i ddangos y `chwaraewyr` sydd ar ôl i ddewis ohonynt.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---