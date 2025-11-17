## Mitspieler

Beginnen wir mit dem Erstellen einer Liste von Spielern, aus denen du wählen kannst.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Du kannst eine Variable verwenden, um eine **Liste** von Spielern zu speichern.

Die Liste sollte in eckigen Klammern stehen. `[]` , mit einem Komma zwischen den Elementen in der Liste.

Beginne, indem du deinem Programm eine Liste von Spielern hinzufügst.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Füge diesen Code hinzu, um deine Variable `spieler` auszugeben:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Du kannst zu einem Element in der Liste gelangen, indem du seine Position in eckigen Klammern nach dem Variablennamen hinzufügst.

Der erste Eintrag in der Liste befindet sich an **Position 0**. Dies unterscheidet sich von Scratch, das mit Position 1 beginnt.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---