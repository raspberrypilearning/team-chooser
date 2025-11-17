## खिलाड़ी

चलो शुरू करते हैं एक सूची बनाकर खिलाड़ियों का चयन करने के लिए 

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

आप खिलाड़ियों की सूची संग्रहीत करने के लिए एक वेरिएबल का उपयोग कर सकते हैं।

सूची वर्ग कोष्ठक (स्क्वायर ब्रैकेट) यानी के ऐसा `[ ]`, में होना चाहिए और प्रत्येक आइटम के बीच एक अल्पविराम यानी के ऐसा ',' के साथ ।

शुरुआत अपने कार्यक्रम में खिलाड़ियों की एक सूची जोड़कर करें।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

अपने खिलाड़ियों का वेरिएबल प्रिंट करने के लिए यह कोड जोड़ें:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

आप सूची में कोई भी आइटम प्राप्त करने के लिए, वेरिएबल के नाम के बाद वर्ग कोष्ठक में उक्त स्थान जोड़ दे

सूची में प्रथम आइटम **position 0** पर है । यह Scratch से अलग है, जो स्थिति 1 पर शुरू होता है।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---