## Scegliere tanti giocatori

Nel seguito dovrai assicurarti che ogni giocatore sia stato scelto per una squadra.

\--- task \---

Evidenzia il tuo codice per scegliere i giocatori per la squadra A e la squadra B e premi il tasto tab per far rientrare (indentare) il codice.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 10-20

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

team_A = [] team_B = []

    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('Players left: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

\--- /code \---

\--- /task \---

\--- task \---

Aggiungi un ciclo **while** per continuare a scegliere i giocatori finché la lunghezza della lista `giocatori` è pari a 0.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 9

## line_highlights: 9

while len(players) > 0: player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

\--- /code \---

\--- /task \---

\--- task \---

Esegui il tuo codice per testarlo. Dovresti vedere che i giocatori vengono selezionati per la squadra A e la squadra B fino a quando non ce ne sono più da scegliere.

    ['Harry', 'Hermione', 'Neville', 'Ginny']
    Hermione
    Players left:  ['Harry', 'Neville', 'Ginny']
    Harry
    Players left:  ['Neville', 'Ginny']
    Ginny
    Players left:  ['Neville']
    Neville
    Players left:  []
    

\--- /task \---

\--- task \---

Add code to print your `team_A` list **after** your `while` loop (making sure it is not indented).

This means that `team_A` will only be printed once, after all the players have been chosen.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 9

## line_highlights: 22

while len(players) > 0: player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

print('Team A', team_A)

\--- /code \---

\--- /task \---

\--- task \---

You can do the same for `team_B`, and you can also delete the other print commands, as they were only there to test your code.

Il tuo codice dovrebbe essere più o meno così:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights:

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']

team_A = [] team_B = []

while len(players) > 0: player_A = choice(players) team_A.append(player_A) players.remove(player_A)

    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)
    

print('Team A', team_A) print('Team B', team_B)

\--- /code \---

\--- /task \---

\--- task \---

Metti alla prova il tuo codice e dovresti vedere solo la tua lista di giocatori assieme ai team finali.

    Team A ['Hermione', 'Harry']
    Team B ['Neville', 'Ginny']
    

\--- /task \---