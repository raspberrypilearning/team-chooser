## Tek oyuncular

Programınızı tek sayıda oyuncu ile çalışacak şekilde geliştirelim.

\--- task \---

+ `oyuncular.txt` dosyanıza bir oyuncu ismi daha ekleyin ki oyuncu sayısı tek sayı olsun.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Kodunuzu test ederseniz, bir hata mesajı aldığınızı göreceksiniz.

![ekran görüntüsü](images/error.png)

\--- /task \---

Bunun nedeni, programınızın A takımı ve ardından B takımı için rastgele oyuncuları seçmeye devam etmesidir. Ancak, eğer eşit sayıda olmayan oyuncular varsa, A takımı için bir oyuncu seçildikten sonra, B takımı için seçilecek oyuncu kalmayacak.

\--- task \---

Bu hatayı düzeltmek için, programınıza `oyuncular` listesi boşalana kadar devam eden `while` döngüsünü `durdurmasını` söyleyebilirsiniz.

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

Kodunuzu tekrar test ederseniz, kodunuzun artık tek sayıda oyuncuyla çalıştığını görmeniz gerekir.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---