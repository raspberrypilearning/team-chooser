## Giocatori dispari

Miglioriamo il tuo programma per lavorare con un numero dispari di giocatori.

\--- task \---

+ Aggiungi un altro nome alla tua lista `giocatori.txt`, in modo da avere un numero dispari di giocatori.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Se esegui il test del codice, vedrai che ricevi un messaggio di errore.

![screenshot](images/error.png)

\--- /task \---

L'errore è dovuto al fatto che il tuo programma continua a scegliere giocatori casuali per la squadra A e poi la squadra B. Tuttavia, se c'è un numero dispari di giocatori, dopo aver scelto un giocatore per la squadra A non rimangono giocatori da scegliere per la squadra B.

\--- task \---

Per correggere questo bug, puoi dire al tuo programma di interrompere (`break`) il tuo ciclo `while` se la lista `giocatori` è vuota.

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

Se testi nuovamente il codice, dovreste vedere che ora funziona con un numero dispari di giocatori.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---