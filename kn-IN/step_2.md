## ಆಟಗಾರರು

ಆಯ್ಕೆ ಮಾಡಲು ಆಟಗಾರರ ಪಟ್ಟಿಯನ್ನು ರಚಿಸುವ ಮೂಲಕ ಪ್ರಾರಂಭಿಸೋಣ.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

ನೀವು ಒಂದು ವೇರಿಯೇಬಲ್ ಅನ್ನು ಸಂಗ್ರಹಿಸಲು ಉಪಯೋಗಿಸಬಹುದು **list** ಆಟಗಾರರು.

ಪಟ್ಟಿ ಚದರ ಆವರಣಗಳಲ್ಲಿರಬೇಕು `[ ]` , ಪಟ್ಟಿಯಲ್ಲಿರುವ ಪ್ರತಿಯೊಂದು ಐಟಂ ನಡುವೆ ಅಲ್ಪವಿರಾಮದಿಂದ.

ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂಗೆ ಆಟಗಾರರ ಪಟ್ಟಿಯನ್ನು ಸೇರಿಸುವ ಮೂಲಕ ಪ್ರಾರಂಭಿಸಿ.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

ನಿಮ್ಮ`players` ವೇರಿಯೇಬಲ್ ಅನ್ನು ಪ್ರಿಂಟ್ ಮಾಡಲು ಈ ಕೋಡ್ ಅನ್ನು ಹಾಕಿ:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

ವೇರಿಯಬಲ್ ಹೆಸರಿನ ನಂತರ ಚದರ ಆವರಣಗಳಲ್ಲಿ ಅದರ ಸ್ಥಾನವನ್ನು ಸೇರಿಸುವ ಮೂಲಕ ನೀವು ಪಟ್ಟಿಯಲ್ಲಿರುವ ಐಟಂ ಅನ್ನು ಪಡೆಯಬಹುದು.

ಪಟ್ಟಿಯಲ್ಲಿನ ಮೊದಲ ಐಟಂ **position 0** ರಲ್ಲಿದೆ. ಇದು ಸ್ಕ್ರ್ಯಾಚ್‌ಗೆ ಭಿನ್ನವಾಗಿದೆ, ಇದು ಸ್ಥಾನ ಒಂದರಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---