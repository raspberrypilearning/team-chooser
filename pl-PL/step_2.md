## Gracze

Zacznijmy od stworzenia listy graczy do wyboru.

\--- task \---

Open the [Team chooser starter](https://editor.raspberrypi.org/en/projects/team-chooser-starter){:target="_blank"} project. The code editor will open in another browser tab.

\--- /task \---

\--- task \---

Możesz użyć zmiennej do przechowywania **listy** graczy.

Lista powinna znajdować się w nawiasach kwadratowych `[ ]`, a między elementami na liście powinny znajdować się przecinki.

Zacznij od dodania listy graczy do twojego programu.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 1

players = ['Harry', 'Hermione']

\--- /code \---

\--- /task \---

\--- task \---

Dodaj poniższy kod, aby wypisać wartość zmiennej `gracze`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 2

players = ['Harry', 'Hermione'] print(players)

\--- /code \---

\--- /task \---

\--- task \---

Aby uzyskać dostęp do któregoś z elementów na liście, wystarczy dodać po nazwie zmienniej kwadratowe nawiasy i podać w nich cyfrę odpowiadającą pozycji tego elementu na liście.

Pierwsza pozycja na liście to **pozycja 0**. To inaczej niż w Scratchu, gdzie zaczynaliśmy od pozycji 1.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4-5

players = ['Harry', 'Hermione'] print(players)

print(players[0]) print(players[1])

\--- /code \---

\--- /task \---