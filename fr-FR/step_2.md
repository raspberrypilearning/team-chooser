## Joueurs

Commençons par créer une liste de joueurs à choisir.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Tu peux utiliser une variable pour stocker une **liste** de joueurs.

La liste doit être dans des crochets `[ ]`, avec une virgule entre chaque élément dans la liste.

Commence par ajouter une liste de joueurs à ton programme.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Ajoute ce code pour afficher ta variable `joueurs`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Tu peux accéder à un élément dans la liste en ajoutant sa position dans les crochets après le nom de la variable.

Le premier élément de la liste est à la **position 0** . Ceci est différent de Scratch, qui commence à la position 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---