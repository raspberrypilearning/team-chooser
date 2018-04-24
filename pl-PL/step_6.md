## Wybieranie wielu graczy

Teraz musisz upewnić się, że każdy gracz został wybrany do zespołu.

+ Zaznacz kod, który wybiera graczy do zespołu A i zespołu B i naciśnij klawisz tabulacji, aby kod był wcięty (przesunięty w prawo).
    
    ![screenshot](images/team-loop-tab.png)

+ Dodaj pętlę **while** (dopóki), aby wybierać graczy do momentu, kiedy długość listy `gracze` będzie wynosić 0.
    
    ![screenshot](images/team-loop-while.png)

+ Uruchom swój kod, aby go przetestować. Powinieneś zobaczyć, że gracze są wybierani do zespołu A i zespołu B tak długo, dopóki nie będzie już więcej graczy do wyboru.
    
    ![screenshot](images/team-loop-test.png)

+ Dodaj kod, który wypisze zawartość listy `zespolA` **zaraz za** pętlą `while` (upewnij się, że nowy kod nie jest wcięty).
    
    Dzięki temu zawartość listy `zespolA` zostanie wyświetlona tylko raz, po wybraniu wszystkich graczy.
    
    ![screenshot](images/team-teamA-paste.png)

+ Możesz zrobić to samo z listą `zespolB`. Możesz też usunąć inne polecenia print, ponieważ były tam tylko po to, aby przetestować twój kod.
    
    Tak powinien wyglądać twój kod:
    
    ![screenshot](images/team-loop-finished.png)

+ Przetestuj swój kod ponownie. Powinieneś zobaczyć tylko listę graczy i składy zespołów.
    
    ![screenshot](images/team-loop-finished-test.png)