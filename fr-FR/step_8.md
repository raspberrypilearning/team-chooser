## Joueurs impair

Améliorons ton programme pour travailler avec un nombre impair de joueurs.

\--- task \---

+ Ajoute un autre nom à ta liste `joueurs.txt `, de sorte que tu as un nombre impair de joueurs.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Si tu testes ton code, tu verras que tu obtiens un message d'erreur.

![capture d'écran](images/error.png)

\--- /task \---

L'erreur est due au fait que ton programme continue de choisir des joueurs aléatoires pour l'équipe A, puis pour l'équipe B. Toutefois, s'il y a un nombre impair de joueurs, après avoir choisi un joueur pour l'équipe A, il ne reste plus aucun joueur à choisir pour l'équipe B.

\--- task \---

Pour corriger ce bug, tu peux indiquer à ton programme de `sortir` de ta boucle `while` si ta liste `joueurs` est vide.

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

Si tu testes à nouveau ton code, tu devrais voir qu'il fonctionne maintenant avec un nombre impair de joueurs.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---