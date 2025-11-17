## Oyuncular

Aralarından seçim yapabileceğimiz bir oyuncu listesi oluşturarak başlayalım.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Oyuncuların **listesini** kaydetmek için bir değişken kullanabilirsiniz.

Bu liste köşeli parantez `[ ]` içinde olmalı ve listedeki her elemanın arasında virgül bulunmalı.

Programınıza bir oyuncu listesi ekleyerek başlayın.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

`oyuncular` değişkeninizi yazdırmak için bu kodu ekleyin:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Listedeki bir öğeye, değişken adından sonra köşeli parantez içindeki konumunu ekleyerek ulaşabilirsiniz.

Listedeki ilk öğe **0 konumunda**'dır. Bu, 1. pozisyondan başlayan Scratch'ten farklıdır.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---