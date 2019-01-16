## Slumpmässiga spelare

Låt oss välja slumpmässiga spelare!

+ För att kunna få en slumpmässig spelare från dina `spelare` lista måste du först importera `val` del av `slumpmässiga` modulen.
    
    ![skärmdump](images/team-import-random.png)

+ För att få en slumpmässig spelare kan du använda `val`. (Du kan också ta bort koden för att skriva ut enskilda spelare.)
    
    ![skärmdump](images/team-random-player.png)

+ Testa ditt `val` kod ett par gånger och du bör se en annan spelare som valts varje gång.

+ Du kan också skapa en ny variabel som heter `playerA`, och använder den för att lagra din slumpmässiga spelare.
    
    ![skärmdump](images/team-random-playerA.png)

+ Du behöver en ny lista för att lagra alla spelare i lag A. Till att börja med ska listan vara tom.
    
    ![skärmdump](images/team-teamA.png)

+ Du kan nu lägga till din slumpmässigt utvalda spelare till `teamA`. För att göra detta kan du använda `teamA.append` (**lägg till** betyder tillägg till slutet).
    
    ![skärmdump](images/team-teamA-add.png)

+ Nu när din spelare har valts kan du ta bort dem från din lista med `spelare`.
    
    ![skärmdump](images/team-players-remove.png)

+ Testa den här koden genom att lägga till ett `skriv` kommando, för att visa de `spelare` kvar att välja mellan.
    
    ![skärmdump](images/team-players-remove-test.png)
    
    I exemplet ovan har Hermione valts för `lagA`, och så har den tagits bort från listan med `spelare`.