## Losowi gracze

Wybierzmy losowych graczy!

+ Aby wybrać losowego gracza z listy `gracze`, najpierw należy zaimportować `choice` z modułu `random`.
    
    ![screenshot](images/team-import-random.png)

+ Aby wybrać losowego gracza, możesz użyć `choice`. (Możesz również usunąć kod, który wypisuje poszczególnych graczy.)
    
    ![screenshot](images/team-random-player.png)

+ Przetestuj swój kod z funkcją `choice` kilka razy, a za każdym razem powinieneś zobaczyć innego gracza.

+ Możesz też utworzyć nową zmienną o nazwie `graczA` i użyć jej do przechowywania wylosowanego gracza.
    
    ![screenshot](images/team-random-playerA.png)

+ Będziesz potrzebować nowej listy do przechowywania wszystkich graczy w zespole A. Na początku ta lista powinna być pusta.
    
    ![screenshot](images/team-teamA.png)

+ Możesz teraz dodać wylosowanego gracza do listy `zespolA`. Aby to zrobić, możesz użyć `zespolA.append` (**append** oznacza dodanie na koniec listy).
    
    ![screenshot](images/team-teamA-add.png)

+ Po wybraniu gracza możesz usunąć go z listy `gracze`.
    
    ![screenshot](images/team-players-remove.png)

+ Przetestuj ten kod, dodając polecenie `print`, aby pokazać, którzy `gracze` nie zostali jeszcze wylosowani.
    
    ![screenshot](images/team-players-remove-test.png)
    
    W powyższym przykładzie Hermiona została wybrana do `zespolA` i została usunięta z listy `gracze`.