## फायली

खेळाडूंची यादी संग्रहीत करण्यासाठी तुम्ही एक फाइल वापरू शकता.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ तुमच्या नवीन फाइल ला तुमचे खेळाडू जोडा. तुमच्या शेवटच्या खेळाडू नंतर रिकामी ओळ नसल्याचे सुनिश्चित करा.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

तुमची `players` यादी बदला जेणेयारून ती रिकामी होईल.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

तुमची `players.txt` फाइल उघडा (`'r'` म्हणजे केवळ-वाचनीय).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

फाइल मधून ती यादी वाचा आणि तुमच्या `players` यादी ला जोडा. (`स्प्लिटलाइन्स(splitlines)` कोडचा अर्थ असा आहे की फाईलमधील प्रत्येक ओळ ही ` players` यादीतील एक नवीन आयटम आहे).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

तुम्ही तुमचा कोडतपासल्यास, त्याने पूर्वीसारखा काम केले पाहिजे. पण, आता तुमच्या `players.txt` फाइलला खेळाडू जोडणे बरेच सोपे आहे.

\--- /task \---