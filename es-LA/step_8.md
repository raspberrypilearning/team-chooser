## Jugadores impares

Mejoremos tu programa para que pueda trabajar con un número impar de jugadores.

\--- task \---

+ Añade otro nombre a tu lista `players.txt`, para que tengas un número impar de jugadores.

## \--- code \---

language: python filename: players.txt line_numbers: true line_number_start: 1

## line_highlights: 5

Harry Hermione Neville Ginny Luna

\--- /code \---

\--- /task \---

\--- task \---

Si pruebas tu código, verás que aparece un mensaje de error.

![captura de pantalla](images/error.png)

\--- /task \---

El error se debe a que tu programa sigue eligiendo jugadores al azar para el equipo A y luego para el equipo B. Sin embargo, si hay un número impar de jugadores, después de elegir un jugador para el equipo A, no quedan jugadores para elegir para el equipo B.

\--- task \---

Para corregir este error, puedes decirle a tu programa que termine `break` tu bucle `while` si tu lista `jugadores` esta vacía.

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

Si vuelves a probar tu código, deberías ver que ahora funciona con un número impar de jugadores.

## \--- code \---

language: python filename: main.py line_numbers: false line_number_start:

## line_highlights:

Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']

\--- /code \---

\--- /task \---