## Dosyalar

Oyuncularınızın listesini kaydetmek için bir dosya kullanabilirsiniz.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Oyuncularınızı yeni dosyanıza ekleyin. Son oyuncunuzdan sonra boş satır olmadığından emin olun.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

`oyuncular` listesi değişkeninin boş olmasını sağlayın.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

`oyuncular.txt` dosyanızı açın (`'r'` ifadesi dosyanın sadece okunabilir olduğu anlamına gelir).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Dosyadaki listeyi okutun ve `oyuncular` listesi değişkenine ekleyin. (`splitlines` kodu, dosyanın içindeki her satırın, `oyuncular` listesinin yeni birer ögesi olduğu anlamına gelir).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Eğer kodunuzu tekrar denerseniz aynı eskisi gibi çalışıyor olmalı. Ancak, şimdi `oyuncular.txt` dosyasına oyuncu eklemek çok daha kolay.

\--- /task \---