## Jucători impari

Să îmbunătățim programul pentru a funcționa cu un număr impar de jucători.

\--- task \---

+ Adaugă un alt nume listei tale `jucatori.txt`, pentru a avea un număr impar de jucători.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Dacă testezi codul, vei vedea că primești un mesaj de eroare.

![captură de ecran](images/error.png)

\--- /task \---

Această eroare se datorează faptului că programul tău alege jucători la întamplare pentru echipele A și B. Cu toate acestea, dacă numărul de jucători este impar, atunci după ce se alege un jucător pentru echipa A, nu mai rămâne niciun jucător de ales pentru echipa B.

\--- task \---

Pentru a rezolva această problemă, îi poți spune programului tău să iasă din din structura ta `while` dacă lista ta de `jucatori` este goală cu ajutorul lui `break`.

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

Dacă testezi codul din nou, ar trebui să vezi că acum funcționează cu un număr impar de jucători.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---