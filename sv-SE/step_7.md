## filer

Du kan använda en fil för att lagra din lista över spelare.

+ Klicka på + -ikonen och skapa en ny fil som heter `players.txt`.
    
    ![skärmdump](images/team-file-create.png)

+ Lägg till dina spelare i din nya fil. Se till att det inte finns någon blank linje efter din sista spelare.
    
    ![skärmdump](images/team-file-add.png)

+ Ändra dina `spelare` lista så att den är tom.
    
    ![skärmdump](images/team-players-empty.png)

+ Öppna `players.txt` fil (den `'r'` sätt skrivskyddad).
    
    ![skärmdump](images/team-file-open.png)

+ Läs listan från filen och lägg till din `spelare` lista. ( `Splitlines` koden betyder att varje rad i filen är ett nytt objekt i listan `spelare`).
    
    ![skärmdump](images/team-file-load.png)

+ Om du testa din kod ska den fungera exakt samma som tidigare. Men nu är det mycket lättare att lägga till spelare i din `players.txt` fil.