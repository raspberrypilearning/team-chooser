## Τυχαίοι παίκτες

Ας επιλέξουμε τυχαίους παίκτες!

\--- task \---

Για να είσαι σε θέση να πάρεις έναν τυχαίο παίκτη από τη λίστα `players`, θα χρειαστεί πρώτα να εισάγεις την `choice` από τη python βιβλιοθήκη `random`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Για να πάρεις έναν τυχαίο παίκτη, μπορείς να χρησιμοποιήσεις την `choice`. (Μπορείς επίσης να διαγράψεις τον κώδικα για να εμφανίσεις μεμονωμένους παίκτες.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Δοκίμασε τον κώδικα με την `choice` μερικές φορές και θα πρέπει να βλέπεις ένα διαφορετικό παίκτη να επιλέγεται κάθε φορά.

\--- /task \---

\--- task \---

Μπορείς επίσης να δημιουργήσεις μια νέα μεταβλητή που ονομάζεται `playerA` για να αποθηκεύεις τον τυχαίο παίκτη σου.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Θα χρειαστείς μια νέα λίστα για να αποθηκεύεις όλους τους παίκτες της ομάδας Α. Αυτή η λίστα στην αρχή πρέπει να είναι κενή.

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

Τώρα μπορείς να προσθέσεις τον τυχαία επιλεγμένο παίκτη σου στη λίστα `teamA`. Για να γίνει αυτό, μπορείς να χρησιμοποιήσεις την εντολή `teamA.append` (**append** σημαίνει προσθήκη στο τέλος).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Τώρα που έχει επιλεγεί ο παίκτης σου, μπορείς να τον αφαιρέσεις από τη λίστα παικτών `players`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Δοκίμασε αυτόν τον κώδικα προσθέτοντας μια εντολή `print`, για να εμφανίσεις τους παίκτες που απέμειναν στη λίστα `players`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---