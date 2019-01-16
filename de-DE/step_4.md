## Zufällig ausgesuchte Mitspieler

Lass uns Spieler zufällig auswählen!

+ Um einen zufälligen Spieler von deiner Liste `spieler` zu bekommen, musst du zuerst den Teil `choice ` des Moduls `random` importieren.
    
    ![screenshot](images/team-import-random.png)

+ Um einen zufälligen Spieler zu erhalten, kannst du die Option `choice` verwenden. (Du kannst den Code zum Ausgeben für aller Spieler auch löschen, um einzelne Spieler auszugeben.)
    
    ![screenshot](images/team-random-player.png)

+ Teste deinen `choice` Code ein paar Mal und es sollte jedes Mal eine anderer Spieler ausgewählt werden.

+ Du kannst auch eine neue Variable mit dem Namen `spielerA` erstellen und sie dann zum Speichern deines zufälligen Spielers zu verwenden.
    
    ![screenshot](images/team-random-playerA.png)

+ Du benötigst eine neue Liste, um alle Spieler in Team A zu speichern. Zunächst sollte diese Liste leer sein.
    
    ![screenshot](images/team-teamA.png)

+ Du kannst jetzt deinen zufällig ausgewählten Spieler zu `teamA` hinzufügen. Dazu kannst du `teamA.append` (**append** bedeutet am Ende hinzufügen).
    
    ![screenshot](images/team-teamA-add.png)

+ Nachdem ein Spieler ausgewählt wurde, kannst du ihn aus der Liste `spieler` entfernen.
    
    ![screenshot](images/team-players-remove.png)

+ Teste diesen Code, indem du eine Ausgabe mit `print` hinzufügst, um die noch auswählbaren Elemente der Liste `spieler` anzuzeigen.
    
    ![screenshot](images/team-players-remove-test.png)
    
    In the example above, Hermione has been chosen for `teamA`, and so has been removed from the list of `players`.