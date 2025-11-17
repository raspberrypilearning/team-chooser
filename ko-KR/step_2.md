## 플레이어

먼저 선택할 플레이어 목록을 만들어 봅시다.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

변수를 사용하여 플레이어의 **리스트**를 저장할 수 있습니다.

목록은 대괄호 `[]`에 있어야하며 목록의 각 항목 사이에 쉼표가 있어야합니다.

먼저 프로그램에 플레이어 목록을 추가하십시오.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

아래 코드로 `플레이어` 변수 내용을 출력하세요:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

변수 이름 뒤 대괄호를 추가하고, 대괄호 안에 위치를 추가하여 리스트의 항목을 가져올 수 있습니다.

리스트의 첫 번째 항목의 **위치는 0에서 시작합니다.** 이는 1에서 위치가 시작하는 스크래치와 다르니 주의하시기 바랍니다.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---