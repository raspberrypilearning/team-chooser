## arquivos

Você pode usar um arquivo para armazenar sua lista de jogadores.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Adicione seus jogadores ao seu novo arquivo. Certifique-se de que não há linha em branco depois do seu último jogador.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Altere sua lista `jogadores` para que ela fique vazia.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Abra o seu arquivo `players.txt` (o `'r'` significa somente leitura).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Leia a lista do arquivo e adicione à sua lista de `jogadores`. (O `splitlines` code significa que cada linha no arquivo é um novo item na lista `jogadores`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Se você testar seu código, ele deve funcionar exatamente como antes. No entanto, agora é muito mais fácil adicionar jogadores ao seu arquivo `players.txt`.

\--- /task \---