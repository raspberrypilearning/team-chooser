## Παίκτες

Ας ξεκινήσουμε δημιουργώντας μια λίστα παικτών για να διαλέξεις.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Μπορείς να χρησιμοποιήσεις μια μεταβλητή για να αποθηκεύσεις μια **λίστα** παικτών.

Η λίστα πρέπει να είναι σε αγκύλες `[]`, με κόμμα ανάμεσα σε κάθε στοιχείο της.

Ξεκίνα προσθέτοντας μια λίστα παικτών στο πρόγραμμά σου.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Πρόσθεσε αυτόν τον κώδικα για να εμφανίσεις τη μεταβλητή `players`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Μπορείς να διαβάσεις ένα στοιχείο της λίστας προσθέτοντας τη θέση του ανάμεσα σε αγκύλες μετά το όνομα της λίστας.

Το πρώτο στοιχείο της λίστας είναι στη θέση **0**. Αυτό είναι διαφορετικό από το Scratch, στο οποίο αρχίζει στη θέση 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---