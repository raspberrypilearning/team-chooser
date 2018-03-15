## Giocatori dispari

Miglioriamo il programma per farlo funzionare con un numero dispari di giocatori.

+ Aggiungi un altro nome alla tua lista 'players.txt', in modo che tu abbia un numero dispari di giocatori.

	![screenshot](images/team-luna.png)

+ Se provi il tuo codice, vedrai che otterrai un messaggio di errore.

	![screenshot](images/team-error.png)

+ L'errore è perché il tuo programma continua a scegliere giocatori a caso per la squadra A e poi la squadra B. Tuttavia, se c'è un numero dispari di giocatori allora dopo aver scelto un giocatore per la squadra A non ci saranno giocatori rimasti per la squadra B.

	per risolvere questo bug, puoi dire al tuo programma che rompa 'break' il tuo loop 'while' se la lista dei tuoi 'players' è vuota.

	![screenshot](images/team-fix.png)

+ Se provi di nuovo il codice, vedrai che adesso funziona con un numero dispari di giocatori.

	![screenshot](images/team-fix-test.png)


