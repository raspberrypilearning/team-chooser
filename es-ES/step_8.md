## Jugadores impares

Mejoremos el programa para que sea capaz de trabajar con un número impar de jugadores.

+ Añade otro nombre a tu lista `players.txt` de modo que tengas un número de jugadores impar.

	![screenshot](images/team-luna.png)

+ Cuando pruebes tu código recibirás un mensaje de error.

	![screenshot](images/team-error.png)

+ El error se debe a que el programa continúa seleccionando jugadores de forma aleatoria para el equipo A y el equipo B. Sin embargo, si existe un número impar de jugadores, después de seleccionar un jugador para el equipo A no existirán jugadores restantes para el equipo B.

	Para solucionarlo, podrás solicitarle al programa que rompa `break` el bucle `while` si la lista `players` está vacía.

	![screenshot](images/team-fix.png)

+ Si vuelves a probar tu código, comprobarás que ahora funciona con un número de jugadores impar.

	![screenshot](images/team-fix-test.png)



