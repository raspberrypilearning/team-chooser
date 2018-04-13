## Dziwni gracze

Poprawmy Twój program, aby działał z nieparzystą liczbą graczy.

+ Dodaj inną nazwę do listy `players.txt` , aby mieć nieparzystą liczbę graczy.
    
    ![zrzut ekranu](images/team-luna.png)

+ Jeśli przetestujesz kod, zobaczysz komunikat o błędzie.
    
    ![zrzut ekranu](images/team-error.png)

+ Błąd polega na tym, że twój program wybiera losowych graczy dla drużyny A, a następnie drużyny B. Jednakże, jeśli jest nieparzysta liczba graczy, to po wybraniu gracza dla drużyny A nie ma już żadnych graczy do wyboru dla drużyny B.
    
    Aby naprawić ten błąd, możesz powiedzieć programowi, aby `przerwał` z `, podczas gdy` zapełnił, jeśli twoja lista `graczy` jest pusta.
    
    ![zrzut ekranu](images/team-fix.png)

+ Jeśli ponownie przetestujesz swój kod, powinieneś zobaczyć, że działa on teraz z nieparzystą liczbą graczy.
    
    ![zrzut ekranu](images/team-fix-test.png)