## अनियमित खिलाड़ी

चलो अनियमित खिलाड़ियों का चयन करें!

\--- task \---

अपने `खिलाड़ियों` की सूची से एक अनियमित खिलाड़ी प्राप्त करने में सक्षम होने के लिए, सबसे पहले आपको `अनियमित` मॉड्यूल के `choice` हिस्से को आयात करने की आवश्यकता होगी।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

एक अनियमित खिलाड़ी प्राप्त करने के लिए, आप `choice` का उपयोग कर सकते हैं। (आप व्यक्तिगत खिलाड़ियों को प्रिंट करने के लिए कोड भी हटा सकते हैं।)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

कई बार अपनी `choice` कोड का परीक्षण करें और आपको हर बार एक अलग खिलाड़ी को चुना जाना चाहिए।

\--- /task \---

\--- task \---

आप `playerA` नामक एक नया वेरिएबल भी बना सकते हैं, और अपने अनियमित खिलाड़ी को स्टोर करने के लिए इसका उपयोग कर सकते हैं।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

Team A के सभी खिलाड़ियों को स्टोर करने के लिए एक नई सूची की आवश्यकता होगी । शुरू करने के लिए, यह सूची खाली होनी चाहिए।

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

अब आप `team A` में अपने अनियमित ढंग से चुने गए खिलाड़ी को जोड़ सकते हैं। ऐसा करने के लिए, आप `teamA.append` का उपयोग कर सकते हैं (**append** का मतलब है अंत में जोड़ें)।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

अब जब आपके खिलाड़ी को चुना गया है, तो आप उन्हें अपनी `खिलाड़ियों` की सूची से हटा सकते हैं।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

एक `print` कमांड जोड़कर इस कोड का परीक्षण करें, बचे हुए `players` में से चुनने के लिए |

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---