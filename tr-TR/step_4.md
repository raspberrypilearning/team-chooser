## Rastgele oyuncular

Rasgele oyuncu seçelim!

\--- task \---

`oyuncular` listenizden rastgele oyuncular seçebilmek için ilk önce `random` modülünün `choise` bölümünü kodlamaya dahil etmeniz gerekiyor.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

Rastgele bir oyuncu elde etmek için `choise` komutunu kullanabilirsiniz. (Ayrıca tek tek oyuncuları yazdıran kodu da silebilirsiniz.)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

Bir kaç kez `choice` kodunuzu deneyin, her seferinde farklı bir oyuncunun seçilmiş olduğunu göreceksiniz.

\--- /task \---

\--- task \---

Rastgele oyuncunuzu kaydetmek için ayrıca yeni bir `Aoyuncusu` değişkeni oluşturabilirsiniz.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

A takımındaki tüm oyuncuları saklamak için yeni bir listeye ihtiyacınız olacak. Başlayabilmek için, bu liste boş olmalıdır.

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

Şimdi rastgele seçilmiş oyuncuları `Atakimi`'na ekleyebilirsiniz. Bunu yapmak için `Atakimi.append` komutunu kullanabilirsiniz (**append** sonuna ekle anlamına gelir).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Artık oyuncunuz seçildiğine göre, onları `oyuncular` listenizden kaldırabilirsiniz.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

`print` komutunu ekleyip, içinden seçim yapmak için `oyuncular` listesindeki kalan oyuncuları göstererek kodunuzu test edin.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---