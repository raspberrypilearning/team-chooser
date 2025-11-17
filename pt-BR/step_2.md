## Jogadores

Vamos começar criando uma lista de jogadores para escolher.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Você pode usar uma variável para armazenar uma **lista** de jogadores.

A lista deve estar entre colchetes `[ ]`, com uma vírgula entre cada item da lista.

Comece adicionando uma lista de jogadores ao seu programa.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Adicione este código para imprimir sua variável `jogadores`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Você pode acessar um item da lista adicionando sua posição entre colchetes após o nome da variável.

O primeiro item da lista está na **posição 0**. Isso é diferente do Scratch, que começa na posição 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---