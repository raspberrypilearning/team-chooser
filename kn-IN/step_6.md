## ಸಾಕಷ್ಟು ಆಟಗಾರರನ್ನು ಆಯ್ಕೆ ಮಾಡುವುದು

ಮುಂದೆ ನೀವು ಪ್ರತಿ ಆಟಗಾರನನ್ನು ತಂಡಕ್ಕೆ ಆಯ್ಕೆ ಮಾಡಲಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು.

\--- task \---

ತಂಡ ಎ ಮತ್ತು ತಂಡ ಬಿ ಗಾಗಿ ಆಟಗಾರರನ್ನು ಆಯ್ಕೆ ಮಾಡಲು ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ಹೈಲೈಟ್ ಮಾಡಿ ಮತ್ತು ಕೋಡ್ ಇಂಡೆಂಟ್ ಮಾಡಲು ಟ್ಯಾಬ್ ಕೀಲಿಯನ್ನು ಒತ್ತಿ.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 10-20

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

team_A = [] team_B = []

    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('Players left: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

\--- /code \---

\--- /task \---

\--- task \---

ಸೇರಿಸಿ ಒಂದು **while** ಲೂಪ್ ಆಟಗಾರರನ್ನು ಆಯ್ಕೆ ಮಾಡುತ್ತಿರಲು `players` ಉದ್ದ ಪಟ್ಟಿ ಅಲ್ಲಿ ಸೊನ್ನೆ ಆಗುವವರೆಗೂ.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 9

## line_highlights: 9

while len(players) > 0: player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

\--- /code \---

\--- /task \---

\--- task \---

ಅದನ್ನು ಪರೀಕ್ಷಿಸಲು ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ಚಲಾಯಿಸಿ. ಹೆಚ್ಚಿನ ಆಟಗಾರರು ಉಳಿದಿಲ್ಲದವರೆಗೆ ಆಟಗಾರರನ್ನು ತಂಡ ಎ ಮತ್ತು ತಂಡ ಬಿ ಗೆ ಆಯ್ಕೆ ಮಾಡುವುದನ್ನು ನೀವು ನೋಡಬೇಕು.

    ['Harry', 'Hermione', 'Neville', 'Ginny']
    Hermione
    Players left:  ['Harry', 'Neville', 'Ginny']
    Harry
    Players left:  ['Neville', 'Ginny']
    Ginny
    Players left:  ['Neville']
    Neville
    Players left:  []
    

\--- /task \---

\--- task \---

Add code to print your `team_A` list **after** your `while` loop (making sure it is not indented).

This means that `team_A` will only be printed once, after all the players have been chosen.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 9

## line_highlights: 22

while len(players) > 0: player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

print('Team A', team_A)

\--- /code \---

\--- /task \---

\--- task \---

You can do the same for `team_B`, and you can also delete the other print commands, as they were only there to test your code.

ನಿಮ್ಮ ಕೋಡ್ ಹೇಗೆ ಕಾಣಬೇಕು ಎಂಬುದು ಇಲ್ಲಿದೆ:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights:

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']

team_A = [] team_B = []

while len(players) > 0: player_A = choice(players) team_A.append(player_A) players.remove(player_A)

    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)
    

print('Team A', team_A) print('Team B', team_B)

\--- /code \---

\--- /task \---

\--- task \---

ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ಮತ್ತೊಮ್ಮೆ ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಆಟಗಾರರ ಪಟ್ಟಿಯನ್ನು ಮತ್ತು ನಿಮ್ಮ ಅಂತಿಮ ತಂಡಗಳನ್ನು ನೀವು ನೋಡಬೇಕು.

    Team A ['Hermione', 'Harry']
    Team B ['Neville', 'Ginny']
    

\--- /task \---