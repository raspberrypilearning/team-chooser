## Giocatori casuali

Scegliamo giocatori casuali!

+ Per essere in grado di ottenere un giocatore casuale dalla tua lista di `giocatori`, per prima cosa devi importare il metodo `choice` contenuto nel modulo `random`.
    
    ![screenshot](images/team-import-random.png)

+ Per ottenere un giocatore casuale, puoi usare `choice`. (Puoi anche cancellare il codice per stampare i singoli giocatori.)
    
    ![screenshot](images/team-random-player.png)

+ Metti alla prova il tuo codice `choice` alcune volte e dovresti verificare che ogni volta viene scelto un giocatore diverso.

+ Puoi anche creare una nuova variabile chiamata `playerA` e usarla per memorizzare il tuo giocatore casuale.
    
    ![screenshot](images/team-random-playerA.png)

+ Avrai bisogno di una nuova lista per archiviare tutti i giocatori della squadra A. Per cominciare, questa lista deve essere vuota.
    
    ![screenshot](images/team-teamA.png)

+ Ora puoi aggiungere il tuo giocatore scelto a caso al `teamA`. Per fare ciò, puoi usare `teamA.append` (**append** significa aggiungere alla fine).
    
    ![screenshot](images/team-teamA-add.png)

+ Ora che il tuo giocatore è stato scelto, puoi rimuoverlo dalla tua lista di `giocatori`.
    
    ![screenshot](images/team-players-remove.png)

+ Prova questo codice aggiungendo un comando `print`, per mostrare i `giocatori` rimasti da scegliere.
    
    ![screenshot](images/team-players-remove-test.png)
    
    Nell'esempio sopra, Hermione è stata scelta per il `teamA`, e così è stata rimossa dalla lista dei `giocatori`.