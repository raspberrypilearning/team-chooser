## Chwaraewyr odrif

Gadewch i ni wella eich rhaglen i weithio gyda nifer od o chwaraewyr.

\--- task \---

+ Ychwanegwch enw arall at eich rhestr `chwaraewyr.txt`, fel bod gennych chi nifer od o chwaraewyr.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Os byddwch chi'n profi eich cod, fe welwch eich bod yn cael neges gwall.

![sgrinlun](images/error.png)

\--- /task \---

Mae'r gwall oherwydd bod eich rhaglen yn parhau i ddewis chwaraewyr ar hap ar gyfer tîm A ac yna tîm B. Fodd bynnag, os oes nifer od o chwaraewyr yna ar ôl dewis chwaraewr ar gyfer tîm A does dim chwaraewyr ar ôl i'w dewis ar gyfer tîm B.

\--- task \---

I atgyweirio'r gwall hwn, gallwch chi ddweud wrth eich rhaglen i `break` (dorri) allan o'ch dolen `while` (tra) dolen os yw eich rhestr `chwaraewyr` yn wag.

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

Os ydych chi'n profi eich cod eto, dylech weld ei fod bellach yn gweithio gyda nifer od o chwaraewyr.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---