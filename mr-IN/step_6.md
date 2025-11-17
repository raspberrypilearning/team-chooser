## बरेच खेळाडू निवडणे

पुढे तुम्हाला हे सुनिश्चित करावा लागेल की प्रत्येक खेळाडू टीमसाठी निवडला गेला आहे.

\--- task \---

team A आणि team B मधून खेळाडू निवडण्यासाठी तुमचं कोड हायलाइट करा आणि कोड ला इंडेंट(indent) करण्यासाठी टॅब की(tab key) दाबा.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 10-20

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

team_A = [] team_B = []

    player_A = choice(players)
    print(player_A)
    team_A.append(player_A)
    players.remove(player_A)
    print('Players left: ', players)
    
    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

\--- /code \---

\--- /task \---

\--- task \---

`players` यादी 0 होई पर्यंत खेळाडू निवडत राहण्यासाठी **व्हाईल(while)** लूप जोडा.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 9

## line_highlights: 9

while len(players) > 0: player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

\--- /code \---

\--- /task \---

\--- task \---

तुमच्या कोड ची चाचणी घेण्यासाठी रन करून बघा. तुम्ही बघू शकाल की कोणतेही खेळाडू शिल्लक नसे पर्यंत team A आणि team B मधले खेळाडू निवडले जात असतील.

    ['Harry', 'Hermione', 'Neville', 'Ginny']
    Hermione
    Players left:  ['Harry', 'Neville', 'Ginny']
    Harry
    Players left:  ['Neville', 'Ginny']
    Ginny
    Players left:  ['Neville']
    Neville
    Players left:  []
    

\--- /task \---

\--- task \---

Add code to print your `team_A` list **after** your `while` loop (making sure it is not indented).

This means that `team_A` will only be printed once, after all the players have been chosen.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 9

## line_highlights: 22

while len(players) > 0: player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

    player_B = choice(players)
    print(player_B)
    team_B.append(player_B)
    players.remove(player_B)
    print('Players left: ', players)
    

print('Team A', team_A)

\--- /code \---

\--- /task \---

\--- task \---

You can do the same for `team_B`, and you can also delete the other print commands, as they were only there to test your code.

तुमचा कोड कसा दिसला पाहिजे हे येथे आहे:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights:

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']

team_A = [] team_B = []

while len(players) > 0: player_A = choice(players) team_A.append(player_A) players.remove(player_A)

    player_B = choice(players)
    team_B.append(player_B)
    players.remove(player_B)
    

print('Team A', team_A) print('Team B', team_B)

\--- /code \---

\--- /task \---

\--- task \---

तुमच्या कोड ची पुन्हा चाचणी केल्या नंतर तुम्हाला तुमच्या खेळाडूंची यादी आणि त्याच बरोबर तुमच्या अंतिम टीम्स देखील दिसतील.

    Team A ['Hermione', 'Harry']
    Team B ['Neville', 'Ginny']
    

\--- /task \---