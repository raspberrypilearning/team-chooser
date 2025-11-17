## Jugadores

Vamos a empezar por crear una lista de jugadores para elegir.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Puedes usar una variable para almacenar una **lista** de jugadores.

La lista debe estar entre corchetes `[ ]`, con una coma entre cada elemento de la lista.

Empieza añadiendo una lista de jugadores a tu programa.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Añade este código para imprimir tu variable de `jugadores`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Puedes acceder a un elemento de la lista agregando su posición entre corchetes después del nombre de la variable.

El primer elemento de la lista se encuentra en la **posición 0**. Esto es diferente a Scratch, que comienza en la posición 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---