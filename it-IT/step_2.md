## Giocatori

Iniziamo creando un elenco di giocatori tra cui scegliere.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

È possibile utilizzare una variabile per memorizzare una **lista** di giocatori.

L'elenco deve essere racchiuso tra parentesi quadre `[]`, con una virgola tra ogni elemento della lista.

Inizia aggiungendo un elenco di giocatori al tuo programma.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Aggiungi questo codice per stampare la variabile `giocatori`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

È possibile ottenere un elemento nell'elenco aggiungendo la sua posizione tra parentesi quadre dopo il nome della variabile.

Il primo elemento dell'elenco è in **posizione 0**. Nota la differenza con Scratch, che inizia dalla posizione 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---