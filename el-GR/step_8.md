## Περιττός αριθμός παικτών

Ας βελτιώσουμε το πρόγραμμά σου ώστε να λειτουργεί και με περιττό αριθμό παικτών.

\--- task \---

+ Πρόσθεσε άλλο ένα όνομα στο αρχείο `players.txt`, ώστε να έχεις περιττό αριθμό παικτών.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Εάν δοκιμάσεις τον κώδικα, θα δεις ότι εμφανίζεται μήνυμα σφάλματος.

![screenshot](images/error.png)

\--- /task \---

Το σφάλμα οφείλεται στο γεγονός ότι το πρόγραμμά σου εξακολουθεί να επιλέγει τυχαίους παίκτες για την ομάδα Α και στη συνέχεια για την ομάδα Β. Ωστόσο, εάν υπάρχει περιττός αριθμός παικτών, τότε μετά την επιλογή παίκτη για την ομάδα Α δεν υπάρχουν παίκτες για την ομάδα Β.

\--- task \---

Για να διορθώσεις αυτό το σφάλμα, μπορείς να πεις στο πρόγραμμά σου να σπάσει με την εντολή `break` το βρόχο `while` μόλις η λίστα παικτών `players` αδειάσει.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 10

## line_highlights: 15-16

while len(players) > 0: player_A = choice(players) team_A.append(player_A) players.remove(player_A)

    if players == []:
        break
    
    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)
    

\--- /code \---

\--- /task \---

\--- task \---

Εάν δοκιμάσεις ξανά τον κώδικα, θα πρέπει τώρα να λειτουργεί και με περιττό αριθμό παικτών.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---