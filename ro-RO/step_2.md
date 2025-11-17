## Jucători

Să începem prin crearea unei liste de jucători din care se va alege.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Poți folosi o variabilă pentru a reține o **listă** de jucători.

Lista trebuie să fie între paranteze drepte `[ ]`, cu o virgulă între fiecare element din listă.

Începe prin a adăuga o listă de jucători la programul tău.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Adaugă acest cod pentru a afișa variabila ta `jucatori`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Poți ajunge la un element din listă prin adăugarea poziției acestuia între paranteze drepte după numele variabilei.

Primul element din listă se află la **poziția 0**. Acest lucru este diferit de Scratch, unde listele încep de la poziția 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---