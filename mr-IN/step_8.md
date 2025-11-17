## विषम खेळाडू

विषम संख्येच्या खेळाडूंसह काम करण्यासाठी तुमचा प्रोग्राम सुधारूया.

\--- task \---

+ तुमच्या `players.txt` मध्ये आणखी एक नाव जोडा जेणेकरून तुमच्याकडे विषम संखेचे खेळाडू होतील.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

तुम्ही तुमच्या कोडची चाचणी घेतल्यास, तुम्हाला एक त्रुटी संदेश(error message) प्राप्त झाल्याचे दिसेल.

![screenshot](images/error.png)

\--- /task \---

त्रुटी(error) ह्यामुळे आहे की तुमचा प्रोग्राम पहिले team A आणि त्या नंतर team B मधून कोणतेही खेळाडू निवडत आहे. पण जर विषम संखेचे खालडू आहेत तर team A मधून एक खेळाडू निवडल्या नंतर team B मधून निवडण्यासाठी काहीच खेळाडू उरत नाहीत.

\--- task \---

जर तुमची `players` यादी रिकामी आहे, तर तुम्ही तुमच्या प्रोग्राम ला `व्हाइल(while)` लूप मधून `बाहेर` यायला सांगू शकता जेणेकरून ह्या बगचं निराकरण होईल.

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

तुम्ही तुमच्या कोड ची पुन्हा तपासणी केल्यास, तुम्हाला दिसेल की ते आता विषम संखेच्या खेळाडूंसह पण काम करत आहे.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---