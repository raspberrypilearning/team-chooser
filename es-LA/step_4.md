## Jugadores aleatorios

¡Vamos a elegir jugadores aleatoriamente!

+ Para poder obtener un jugador aleatorio de tu lista `jugadores`, primero tienes que importar `choice` que es parte del módulo `random`.
    
    ![captura de pantalla](images/team-import-random.png)

+ Para obtener un jugador aleatorio, puedes utilizar `choice`. (También puedes eliminar el código para imprimir jugadores individuales.)
    
    ![captura de pantalla](images/team-random-player.png)

+ Prueba tu código `choice` varias veces y deberías ver a un jugador diferente cada vez.

+ También puedes crear una nueva variable llamada `jugadorA`, y usarla para guardar tu jugador aleatorio.
    
    ![captura de pantalla](images/team-random-playerA.png)

+ Necesitarás una nueva lista para almacenar a todos los jugadores en el equipo A. Para empezar, esta lista debe estar vacía.
    
    ![captura de pantalla](images/team-teamA.png)

+ Ahora puedes añadir tu jugador elegido al azar a `equipoA`. Para hacer esto, puedes usar `equipoA.append` (**append** significa añadir al final).
    
    ![captura de pantalla](images/team-teamA-add.png)

+ Ahora que su jugador ha sido elegido, puede eliminarlo de su lista de ` jugadores `.
    
    ![captura de pantalla](images/team-players-remove.png)

+ Prueba este código añadiendo un comando `print`, para mostrar los `jugadores` que quedan por elegir.
    
    ![captura de pantalla](images/team-players-remove-test.png)
    
    En el ejemplo anterior, Hermione ha sido elegida para el `equipoA`, y ha sido eliminada de la lista de `jugadores`.