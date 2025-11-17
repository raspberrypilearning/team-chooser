## الملفات

يمكنك استخدام ملف لتخزين قائمة من اللاعبين.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ أضف لاعبيك إلى ملفك الجديد. تأكد من عدم وجود سطر فارغ بعد آخر لاعب.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

غير قائمة `اللاعبين` الخاصة بك بحيث تكون فارغة.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

افتح ملف ` players.txt الخاص بك `(` "R" ` يعني للقراءة فقط).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

اقرأ القائمة من الملف وأضفها إلى قائمة `اللاعبين` الخاصة بك. (كود ال`splitlines` يعني ان كل سطر في الملف هو عنصر جديد في قائمة `اللاعبين`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

إذا قمت باختبار التعليمات البرمجية الخاصة بك، فإنها تنبغي أن تعمل بالضبط كما عملت قبل. ومع ذلك، الآن أسهل بكثير إضافة لاعبين إلى ملف `players.txt`.

\--- /task \---