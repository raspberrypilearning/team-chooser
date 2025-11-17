## Oneven aantal spelers

We gaan het programma verbeteren zodat we met een oneven aantal spelers kunnen werken.

\--- task \---

+ Voeg een andere naam toe aan je `spelers.txt` lijst, zodat je een oneven aantal spelers hebt.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Als je de code test zie je een foutmelding.

![screenshot](images/error.png)

\--- /task \---

De fout is dat je programma willekeurige spelers blijft kiezen voor team A en dan team B. Maar bij een oneven aantal spelers zijn er na het kiezen van een speler voor team A geen spelers meer over om uit te kiezen voor team B.

\--- task \---

Om deze bug te verhelpen, kun je met `break` uit de `while` lus komen als de `spelers` lijst leeg is.

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

Als je de code opnieuw test, zou je moeten zien dat die nu werkt met een oneven aantal spelers.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---