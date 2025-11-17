## Nieparzyści gracze

Udoskonalmy twój program, aby działał z nieparzystą liczbą graczy.

\--- task \---

+ Dodaj kolejne imię do listy `gracze.txt` tak, aby mieć nieparzystą liczbę graczy.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Jeśli przetestujesz kod, zobaczysz komunikat o błędzie.

![zrzut ekranu](images/error.png)

\--- /task \---

Błąd polega na tym, że twój program wybiera losowych graczy do zespołu A, a następnie do zespołu B. Jeśli jednak liczba graczy jest nieparzysta, to po wybraniu gracza do zespołu A nie ma już żadnych graczy do wyboru do zespołu B.

\--- task \---

Aby naprawić ten błąd, możesz powiedzieć programowi, aby przerwał (ang. `break`) wykonywanie kodu w pętli `while`, jeśli twoja lista `gracze` jest pusta.

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

Kiedy ponownie przetestujesz swój kod, powinieneś zobaczyć, że działa on teraz poprawnie z nieparzystą liczbą graczy.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---