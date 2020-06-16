## Jugadores impares

Mejoremos tu programa para que pueda trabajar con un número impar de jugadores.

+ Añade otro nombre a tu lista `players.txt`, para que tengas un número impar de jugadores.
    
    ![captura de pantalla](images/team-luna.png)

+ Si pruebas tu código, verás que aparece un mensaje de error.
    
    ![captura de pantalla](images/team-error.png)

+ El error se debe a que tu programa sigue eligiendo jugadores al azar para el equipo A y luego para el equipo B. Sin embargo, si hay un número impar de jugadores, después de elegir un jugador para el equipo A, no quedan jugadores para elegir para el equipo B.
    
    Para corregir este error, puedes decirle a tu programa que termine `break` tu bucle `while` si tu lista `jugadores` esta vacía.
    
    ![captura de pantalla](images/team-fix.png)

+ Si vuelves a probar tu código, deberías ver que ahora funciona con un número impar de jugadores.
    
    ![captura de pantalla](images/team-fix-test.png)