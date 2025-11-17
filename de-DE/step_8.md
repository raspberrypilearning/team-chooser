## Ungerade Anzahl an Mitspielern

Lass uns dein Programm verbessern, um mit einer ungeraden Anzahl von Spielern arbeiten zu können.

\--- task \---

+ Füge einen anderen Namen zu deiner Liste in `spieler.txt`, so dass eine ungerade Anzahl von Spielern hast.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Wenn du deinen Code testest, wird eine Fehlermeldung angezeigt.

![Screenshot](images/error.png)

\--- /task \---

Der Fehler liegt darin, dass dein Programm abwechselnd zufällige Spieler für Team A und dann Team B auswählt. Wenn jedoch eine ungerade Anzahl von Spielern vorhanden ist, kannst du nach Auswahl des letzten Spielers für Team A keinen Spieler mehr für Team B auswählen.

\--- task \---

Um diesen Fehler zu beheben, kannst du dein Programm anweisen mittels `break` die `while` Schleife zu verlassen, wenn die Liste deiner `Spieler` leer ist.

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

Wenn du deinen Code erneut testest, solltest du feststellen, dass er jetzt auch mit einer ungeraden Anzahl von Spielern funktioniert.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---