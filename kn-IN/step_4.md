## ಸ್ವೇಚ್ಛೆಯಾದ ಆಟಗಾರರು

ಸ್ವೇಚ್ಛೆಯಾದ ಆಟಗಾರನನ್ನು ಆಯ್ಕೆ ಮಾಡೋಣ!

\--- task \---

ಸ್ವೇಚ್ಛೆಯಾದ ಆಟಗಾರರನ್ನು ತರಲು ನಿಮ್ಮ `players` ಪಟ್ಟೆಇಂದ, ಮೊದಲು ನೀವು `choice` ಭಾಗವನ್ನು ಇಂಪೋರ್ಟ್ ಮಾಡಬೇಕು `ಸ್ವೇಚ್ಛೆಯಾದ` ಘಟಕ ಇಂದ.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

ಸ್ವೇಚ್ಛೆಯಾದ ಆಟಗಾರರನ್ನು ತರಲು ನೀವು `choice`ಉಪಯೋಗಿಸಬಹುದು. (ನೀವು ಕೋಡ್ ಅನ್ನು ಸಹ ಅಳಿಸಬಹುದು ವಯಕ್ತಿಕ ಆಟಗಾರರನ್ನು ಮುದ್ರಿಸಲು.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

ಪರೀಕ್ಷಿಸಿ ನಿಮ್ಮ `choice` ಕೋಡ್ ಕೆಲವು ಬಾರಿ ಮತ್ತೆ ನೀವು ಕಾಣಬೇಕು ಪ್ರತಿಸಲ ಬೇರೆ ಆಟಗಾರರು ಆಯ್ಕೆ ಆಗುತ್ತಿರುವುದನ್ನು.

\--- /task \---

\--- task \---

ನೀವು ಒಂದು ಹೊಸ ವೇರಿಯೇಬಲ್ ಅನ್ನು ತಯಾರಿಸಬಹುದು `playerA`, ಮತ್ತು ಅದನ್ನು ಉಪಯೋಗಿಸಬಹುದು ಸ್ವೇಚ್ಛೆಯಾದ ಆಟಗಾರನನ್ನು ಸಂಗ್ರಹಿಸಲು.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

ಎ ತಂಡದಲ್ಲಿ ಎಲ್ಲ ಆಟಗಾರರನ್ನು ಸಂಗ್ರಹಿಸಲು ನಿಮಗೆ ಹೊಸ ಪಟ್ಟಿ ಅಗತ್ಯವಿದೆ. ಪ್ರಾರಂಭಿಸಲು, ಈ ಪಟ್ಟಿ ಖಾಲಿಯಾಗಿರಬೇಕು.

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

ನೀವು ಸ್ವೇಚ್ಛೆಯಾದ ಆಟಗಾರನನ್ನು ಸಹ ಸೇರಿಸಬಹುದು `teamA` ಗೆ. ಇದನ್ನು ಮಾಡಲು,ನೀವು ಉಪಯೋಗಿಸಬಹುದು `teamA.append` (**append** ಅಂದ್ರೆ ಕೊನೆಗೆ ಸೇರಿಸಿ ಯಂದು).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

ಈಗ ನಿಮ್ಮ ಆಟಗಾರನನ್ನು ಆಯ್ಕೆ ಮಾಡಲಾಗಿರುವುದರಿಂದ, ನೀವು ಅವರನ್ನು ನಿಮ್ಮ `players` ಪಟ್ಟಿ ಇಂದ ತೆಗೆಯಬಹುದು.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

ಪರೀಕ್ಷೆ ಮಾಡಿ ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು `print` ಕಮಾಂಡ್ ಅನ್ನು ಸೇರಿಸುವುದರ ಮೂಲಕ, ಉಳಿದಿದ್ದ `players` ಅನ್ನು ಆಯ್ಕೆ ಮಾಡಲು.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---