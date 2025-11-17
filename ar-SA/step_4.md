## لاعبون عشوائيون

دعونا نختار لاعبين عشوائيين!

\--- task \---

لتكون قادرًا على الحصول على لاعب عشوائي قائمة اللاعبين الخاصة بك, اولاً تحتاج لاستيراد جزئية `الاختيار` من وحدة `random `.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---

\--- task \---

للحصول على لاعب عشوائي, يمكنك استخدام `choice`. (يمكنك أيضا حذف التعليمات البرمجية لطباعة لاعبين منفردين)

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

print(choice(players))

\--- /code \---

\--- /task \---

\--- task \---

اختبر تعليمات `choice` البرمجية الخاصة بك بضع مرات، ويجب أن ترى لاعب مختلف يتم اختياره في كل مرة.

\--- /task \---

\--- task \---

يمكنك أيضًا إنشاء متغير جديد يسمى ` playerA ` ، واستخدامه لتخزين لاعب عشوائي.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 6-7

from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny'] print(players)

player_A = choice(players) print(player_A)

\--- /code \---

\--- /task \---

\--- task \---

ستحتاج إلى قائمة جديدة لتخزين جميع اللاعبين في الفريق A. للبدء ، يجب أن تكون هذه القائمة فارغة.

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

يمكنك الآن إضافة لاعبك المختار عشوائياً إلى ` teamA `. للقيام بذلك ، يمكنك استخدام ` teamA.append ` (** append ** يعني إضافة إلى النهاية).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 10

player_A = choice(players) print(player_A) team_A.append(player_A)

\--- /code \---

\--- /task \---

\--- task \---

الآن بعد أن تم اختيار اللاعب الخاص بك ، يمكنك إزالته من قائمة اللاعبين ` الخاصة بك `.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 11

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A)

\--- /code \---

\--- /task \---

\--- task \---

اختبر هذا الرمز عن طريق إضافة امر ` طباعة `, لاظهار `اللاعبين` المتبقين للاختيار منهم.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 8

## line_highlights: 12

player_A = choice(players) print(player_A) team_A.append(player_A) players.remove(player_A) print('Players left: ', players)

\--- /code \---

\--- /task \---