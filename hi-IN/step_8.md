## विषम (जो पूर्ण रूप से 2 से विभाजित न हो) खिलाड़ी

खिलाड़ियों की विषम संख्या के साथ काम करने के लिए अपने कार्यक्रम में सुधार करें।

\--- task \---

+ अपने `players.txt` सूची में एक और नाम जोड़ें, ताकि आपके पास विषम संख्या में खिलाड़ी हों।

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

यदि आप अपने कोड का परीक्षण करते हैं, तो आप देखेंगे कि आपको एक त्रुटि (error) संदेश मिलेगा।

![स्क्रीनशॉट](images/error.png)

\--- /task \---

त्रुटि इसलिए है क्योंकि आपका प्रोग्राम team A और फिर team B के लिए अनियमित खिलाड़ियों का चयन करता रहता है। हालांकि, अगर खिलाड़ियों की एक विषम संख्या है, तो team A के लिए खिलाड़ी चुनने के बाद team B के लिए चुनने के लिए कोई खिलाड़ी नहीं बचते हैं।

\--- task \---

इस बग को ठीक करने के लिए, आप अपने प्रोग्राम को `while` लूप से `break` कर सकते हैं यदि आपके ` players` की सूची खाली है।

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

यदि आप अपने कोड का फिर से परीक्षण करते हैं, तो आप देखेंगे कि यह अब खिलाड़ियों की विषम संख्या के साथ काम कर रहा है।

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---