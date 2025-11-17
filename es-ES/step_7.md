## Archivos

Puedes usar un archivo para almacenar tu lista de jugadores.

\--- task \---

Click **Add file** and create a new file called `players.txt`.

![Add file button shown beneath the Project files menu](images/Add_file.png)

\--- /task \---

\--- task \---

+ Añade tus jugadores a tu nuevo archivo. Asegúrate de que no haya una línea en blanco después de tu último jugador.

![screenshot showing the names in players.txt](images/players_file.png)

\--- /task \---

\--- task \---

Cambia tu lista `jugadores` para que esté vacía.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 3

from random import choice

players = []

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Abre tu archivo `players.txt` (la `'r'` significa solo lectura).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 4

from random import choice

players = [] file = open('players.txt', 'r')

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Lee la lista del archivo y añadela a tu lista `jugadores`. (El código `splitlines` significa que cada línea en el archivo es un elemento nuevo en la lista `jugadores`).

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 1

## line_highlights: 5

from random import choice

players = [] file = open('players.txt', 'r') players = file.read().splitlines()

team_A = [] team_B = []

\--- /code \---

\--- /task \---

\--- task \---

Si pruebas tu código, debería funcionar exactamente igual que antes. Sin embargo, ahora es mucho más fácil añadir jugadores a tu archivo `players.txt`.

\--- /task \---