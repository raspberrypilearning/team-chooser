## Επιλογή πολλών παικτών

Στη συνέχεια θα πρέπει να βεβαιωθείς ότι κάθε παίκτης έχει επιλεγεί για μια ομάδα.

\--- task \---

Επέλεξε τον κώδικα για την επιλογή παικτών για την ομάδα Α και την ομάδα Β και πάτησε το πλήκτρο tab για να κάνεις μια εσοχή.

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

Πρόσθεσε ένα βρόχο **while** για να επιλέγεις παίκτες μέχρις ότου το πλήθος της λίστας παικτών `players` γίνει 0.

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

Εκτέλεσε τον κώδικα για να τον δοκιμάσεις. Θα πρέπει να βλέπεις παίκτες να επιλέγονται για την ομάδα Α και την ομάδα Β μέχρι να μην έχει απομείνει κανένας.

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

Έτσι πρέπει να φαίνεται ο κώδικας:

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

Δοκίμασε ξανά τον κώδικα και θα πρέπει να βλέπεις μόνο τη λίστα των παικτών καθώς και τις τελικές ομάδες.

    Team A ['Hermione', 'Harry']
    Team B ['Neville', 'Ginny']
    

\--- /task \---