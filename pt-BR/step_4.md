## Jogadores aleatórios

Vamos escolher jogadores aleatórios!

\--- task \---

Para conseguir obter um usuário aleatório da sua lista de `jogadores`, primeiro você precisa importar o `choice` que faz parte do módulo `random`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Para obter um jogador aleatório, você pode usar a `choice`. (Você também pode excluir o código para imprimir jogadores individuais.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Teste seu código `choice` algumas vezes e você verá um jogador diferente sendo escolhido a cada vez.

\--- /task \---

\--- task \---

Você também pode criar uma nova variável chamada `jogadorA` e usá-la para armazenar seu player aleatório.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Você precisará de uma nova lista para armazenar todos os jogadores da equipe A. Para começar, essa lista deve estar vazia.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

team_A = []

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Agora você pode adicionar seu jogador escolhido aleatoriamente ao `timeA`. Para fazer isso, você pode usar `timeA.append` (**append** significa adicionar ao final).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Agora que seu jogador foi escolhido, você pode removê-lo de sua lista de `jogadores`.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Teste este código adicionando um comando `print`, para mostrar os `jogadores` restantes para escolher.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---