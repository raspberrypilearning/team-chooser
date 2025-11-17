## Spelers

We beginnen met het maken van een lijst met spelers om uit te kiezen.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Je kunt een variabele gebruiken om een ​​ **lijst** van spelers in op te slaan.

De lijst moet tussen vierkante haakjes `[ ]`staan, met een komma tussen elk item in de lijst.

Begin met het toevoegen van een lijst met spelers aan het programma.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Voeg deze code toe om de `spelers` variabele weer te geven:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Je kunt een item uit de lijst kiezen door diens positie toe te voegen achter de naam van de variabele, tussen vierkante haken.

Het eerste item in de lijst is op **positie 0**. Dat is anders dan bij Scratch, daar is de start op positie 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---