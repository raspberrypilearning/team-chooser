## फ़ाइलें

आप अपने खिलाड़ियों की सूची को संग्रहीत करने के लिए एक फ़ाइल का उपयोग कर सकते हैं।

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ अपनी नई फ़ाइल में अपने खिलाड़ियों को जोड़ें। सुनिश्चित करें कि आपके अंतिम खिलाड़ी के बाद कोई खाली लाइन नहीं है।

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

अपने `players` की सूची बदलें ताकि यह खाली हो।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

अपनी ` players.txt` फाइल खोलें (`'r'` का मतलब है केवल पढ़ने वाला फाइल) ।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

फ़ाइल से सूची पढ़ें और अपने `players` की सूची में जोड़ें। (`splitlines` कोड का मतलब है कि फाइल में हर लाइन `players` लिस्ट में एक नया आइटम है ।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

यदि आप अपने कोड का परीक्षण करते हैं, तो यह पहले की तरह ही काम करना चाहिए। हालांकि, अब अपने `players.txt` फ़ाइल में खिलाड़ियों को जोड़ना बहुत आसान है।

\--- /task \---