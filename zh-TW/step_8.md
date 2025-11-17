## 奇數數量的隊員

讓我們改進你的程式，使它還能夠處理隊員人數為奇數的情況。

\--- task \---

+ 向你的`players.txt`列表檔案中再新增一個隊員名字，隊員人數就是奇數了。

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

如果測試你的程式碼，你將看到一條錯誤資訊。

![截圖](images/error.png)

\--- /task \---

這個錯誤是因為你的程式一直迴圈在為A隊和B隊選擇隨機隊員，如果隊員總數為奇數的話，在最後一輪中當為A隊選好隊員之後B隊就沒有隊員可以選擇了。

\--- task \---

要修復這個錯誤，你可以告訴你的程式如果`players`列表為空，則使用`break`來中斷你的`while`迴圈。

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

當你再次測試你的程式碼，你應該看到現在它可以處理隊員人數為奇數的情況了。

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---