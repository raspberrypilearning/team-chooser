## اللاعبون

لنبدأ بإنشاء قائمة من اللاعبين للاختيار من بينها.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

يمكنك استخدام متغير لتخزين **قائمة** من اللاعبين.

يجب أن تكون القائمة بين أقواس مربعة `[]` ، مع فاصلة بين كل عنصر في القائمة.

ابدأ بإضافة قائمة باللاعبين إلى برنامجك.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

إضافة هذه التعليمة البرمجية لطباعة متغير `اللاعبين` الخاصة بك:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

يمكنك الوصول إلى عنصر في القائمة بإضافة موضعه بين أقواس مربعة بعد اسم المتغير.

العنصر الأول في القائمة هو في **الموضع 0**. هذا يختلف عن سكراتش ، التي تبدأ في الموضع 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---