## ಬೆಸ ಆಟಗಾರರು

ಬೆಸ ಸಂಖ್ಯೆಯ ಆಟಗಾರರೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಸುಧಾರಿಸೋಣ.

\--- task \---

+ ಇನ್ನೊಂದು ಹೆಸರು ಸೇರಿಸಿ ನಿಮ್ಮ `players.txt` ಪಟ್ಟಿಆದ ರಿಂದ ನೀವು ಬೆಸ ಸಂಖ್ಯಯ ಆಟಗಾರರನ್ನು ಹೊಂದಬಹುದು.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ನೀವು ಪರೀಕ್ಷಿಸಿದರೆ, ನೀವು ದೋಷ ಸಂದೇಶವನ್ನು ಪಡೆಯುತ್ತೀರಿ ಎಂದು ನೀವು ನೋಡುತ್ತೀರಿ.

![screenshot](images/error.png)

\--- /task \---

ದೋಷವೆಂದರೆ ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ತಂಡ ಎ ಮತ್ತು ನಂತರ ತಂಡ ಬಿ ಗೆ ಸ್ವಚ್ಛೆಹಾಗಿ ಆಟಗಾರರನ್ನು ಆಯ್ಕೆ ಮಾಡುತ ಇರುತ್ತದೆ. ಆದಾಗ್ಯೂ, ಬೆಸ ಸಂಖ್ಯೆಯ ಆಟಗಾರರು ಇದ್ದರೆ ತಂಡ ಎಗಾಗಿ ಆಟಗಾರನನ್ನು ಆಯ್ಕೆ ಮಾಡಿದ ನಂತರ ತಂಡ ಬಿ ಗೆ ಆಯ್ಕೆ ಮಾಡಲು ಯಾವುದೇ ಆಟಗಾರರು ಉಳಿದಿಲ್ಲ.

\--- task \---

ಇದನ್ನು ಸರಿಪಡಿಸಲು, ನೀವು ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಮ್ ಗೆ ಹೇಳಬಹುದು `break` ನಿಮ್ಮ ಹೊರಗೆ `while` ಲೂಪ್ ಏನಾದರು ನಿಮ್ಮ `players` ಪಟ್ಟಿ ಖಾಲಿ ಆದಲ್ಲಿ.

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

ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ನೀವು ಮತ್ತೆ ಪರೀಕ್ಷಿಸಿದರೆ, ಅದು ಈಗ ಬೆಸ ಸಂಖ್ಯೆಯ ಆಟಗಾರರೊಂದಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಎಂದು ನೀವು ನೋಡಬೇಕು.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---