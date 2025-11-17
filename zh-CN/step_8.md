## 奇数数量的队员

让我们改进你的程序使它还能够处理数量为奇数的队员。

\--- task \---

+ 向你的`players.txt`列表文件中再添加一个队员名字，这样你就有了奇数数量的队员。

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

如果测试你的代码，你将看到一条错误信息。

![截图](images/error.png)

\--- /task \---

这个错误是因为你的程序一直循环在为A队和B队选择随机队员，如果队员总数为奇数的话，在最后一轮中当为A队选好队员之后B队就没有队员可以选择了。

\--- task \---

要修复这个错误，你可以告诉你的程序如果`players`列表为空，则使用`break`来跳出你的`while`循环、

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

当你再次测试你的代码，你应该看到现在它可以处理奇数数量的队员了。

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---