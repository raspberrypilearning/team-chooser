## Zufällig ausgesuchte Mitspieler

Lass uns Spieler zufällig auswählen!

+ Um einen zufälligen Spieler von deiner Liste `spieler` zu bekommen, musst du zuerst den Teil `choice ` des Moduls `random` importieren.
    
    ![screenshot](images/team-import-random.png)

+ Um einen zufälligen Spieler zu erhalten, kannst du die Option `choice` verwenden. (Du kannst den Code zum Ausgeben für aller Spieler auch löschen, um einzelne Spieler auszugeben.)
    
    ![screenshot](images/team-random-player.png)

+ Teste deinen `choice` Code ein paar Mal und es sollte jedes Mal eine anderer Spieler ausgewählt werden.

+ Du kannst auch eine neue Variable mit dem Namen `spielerA` erstellen und sie dann zum Speichern deines zufälligen Spielers zu verwenden.
    
    ![screenshot](images/team-random-playerA.png)

+ You'll need a new list to store all of the players in team A. To start with, this list should be empty.
    
    ![screenshot](images/team-teamA.png)

+ You can now add your randomly chosen player to `teamA`. To do this, you can use `teamA.append` (**append** means add to the end).
    
    ![screenshot](images/team-teamA-add.png)

+ Now that your player has been chosen, you can remove them from your list of `players`.
    
    ![screenshot](images/team-players-remove.png)

+ Test this code by adding a `print` command, to show the `players` left to choose from.
    
    ![screenshot](images/team-players-remove-test.png)
    
    In the example above, Hermione has been chosen for `teamA`, and so has been removed from the list of `players`.