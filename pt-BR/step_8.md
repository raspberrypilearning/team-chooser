## Jogadores ímpares

Vamos melhorar seu programa para trabalhar com um número ímpar de jogadores.

\--- task \---

+ Adicione outro nome à sua lista `jogadores.txt` , para que você tenha um número ímpar de jogadores.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Se você testar seu código, verá uma mensagem de erro.

![screenshot](images/error.png)

\--- /task \---

O erro ocorre porque seu programa continua escolhendo jogadores aleatórios para a equipe A e depois para a equipe B. No entanto, se houver um número ímpar de jogadores, depois de escolher um jogador para a equipe A, não há mais jogadores para escolher para a equipe B.

\--- task \---

Para corrigir esse bug, você pode dizer ao seu programa para `quebrar` de seu `enquanto` loop se sua lista `jogadores` estiver vazia.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 10

## line_highlights: 15-16

while len(players) > 0: player_A = choice(players) team_A.append(player_A) players.remove(player_A)

    if players == []:
        break
    
    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)
    

\--- /code \---

\--- /task \---

\--- task \---

Se você testar seu código novamente, verá que agora ele funciona com um número ímpar de jogadores.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---