## बहुत से खिलाड़ी चुनना

इसके बाद आपको यह सुनिश्चित करना होगा कि हर खिलाड़ी को टीम के लिए चुना गया है।

\--- task \---

Team Aऔर team B के लिए खिलाड़ियों को चुनने के लिए अपने कोड को हाइलाइट करें और कोड को इंडेंट (indent) करने के लिए टैब (tab) बटन दबाएं।

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

खिलाड़ियों की सूची की लंबाई 0 होने तक `खिलाड़ियों` (players) को चुनने के लिए **while** लूप जोड़ें।

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

इसका परीक्षण करने के लिए अपना कोड चलाएं। आपको team A और team B के लिए चुने गए खिलाड़ियों को तब तक देखना चाहिए जब तक कि कोई और खिलाड़ी न बचे।

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

यहाँ दिखाया गया है कि आपका कोड कैसा दिखेगा:

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

अपने कोड का फिर से परीक्षण करें और आपको अपनी खिलाड़ियों की सूची के साथ-साथ अपनी अंतिम टीमों को भी देखना चाहिए।

    Team A ['Hermione', 'Harry']
    Team B ['Neville', 'Ginny']
    

\--- /task \---