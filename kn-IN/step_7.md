## ಕಡತಗಳನ್ನು(Files)

ನಿಮ್ಮ ಆಟಗಾರರ ಪಟ್ಟಿಯನ್ನು ಸಂಗ್ರಹಿಸಲು ನೀವು ಫೈಲ್ ಅನ್ನು ಬಳಸಬಹುದು.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ ನಿಮ್ಮ ಹೊಸ ಫೈಲ್‌ಗೆ ನಿಮ್ಮ ಆಟಗಾರರನ್ನು ಸೇರಿಸಿ. ನಿಮ್ಮ ಕೊನೆಯ ಆಟಗಾರನ ನಂತರ ಯಾವುದೇ ಖಾಲಿ ಸಾಲು ಇಲ್ಲ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

ಬದಲಾಯಿಸಿಕೊಲ್ಲಿ ನಿಮ್ಮ `players` ಪಟ್ಟಿಯನ್ನುಆದುದರಿಂದ ಅದು ಖಾಲಿ ಆಗಲಿ ಯಂದು.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

ತೆಗೆಯಿರಿ ನಿಮ್ಮ `players.txt` ಫೈಲ್ (ಇಲ್ಲಿ `'r'` ಯಂದರೆ ಬರಿ ಓದಿ ಯಂದು ಅರ್ಥ).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

ಫೈಲ್‌ನಿಂದ ಪಟ್ಟಿಯನ್ನು ಓದಿ ಮತ್ತು ನಿಮ್ಮ `players` ಪಟ್ಟಿಗೆ ಸೇರಿಸಿ. (`splitlines` ಕೋಡ್ ಎಂದರೆ ಫೈಲ್‌ನ ಪ್ರತಿಯೊಂದು ಸಾಲು ` players`ಪಟ್ಟಿ ಹೊಸ ಐಟಂ ಆಗಿದೆ).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ನೀವು ಪರೀಕ್ಷಿಸಿದರೆ, ಅದು ಮೊದಲಿನಂತೆಯೇ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ. ಹೇಗಿದ್ದರೂ,ಈಗ ಆಟಗಾರಗನ್ನು `players.txt` ಫೈಲ್ ಗೆ ಸೇರಿಸುವುದು ಇನ್ನು ಸುಲಭ.

\--- /task \---