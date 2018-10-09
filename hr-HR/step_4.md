## Nasumični igrači

Odaberimo sada nasumično igrače timova!

+ Kako bi nasumično odabrali igrača iz liste `igraci`, prvo je potrebno uvesti naredbu `choice` iz modula `random`.
    
    ![screenshot](images/team-import-random.png)

+ Koristi `choice` da bi dobio nasumičnog igrača. (Možeš i obrisati kôd koji ispisuje pojedinačne igrače.)
    
    ![screenshot](images/team-random-player.png)

+ Isprobaj svoj `choice` kôd nekoliko puta i vidjet ćeš da je svaki put odabran drugi igrač.

+ Možeš kreirati novu varijablu imena `igracA` u koju ćeš spremiti nasumičnog igrača.
    
    ![screenshot](images/team-random-playerA.png)

+ Za spremanje svih igrača iz tima A, moraš napraviti novu listu. Za početak, ova lista mora biti prazna.
    
    ![screenshot](images/team-teamA.png)

+ Sada možeš dodati nasumično odabranog igrača u `tim A`. To češ napraviti koristeći `timA.append`(**append** znači dodati na kraj).
    
    ![screenshot](images/team-teamA-add.png)

+ Sada je igrač izabran i možeš ga maknuti sa liste `igraci`.
    
    ![screenshot](images/team-players-remove.png)

+ Testiraj kôd dodavanjem naredbe `print` i provjeri koji su ti `igraci` preostali.
    
    ![screenshot](images/team-players-remove-test.png)
    
    U primjeru iznad, Ivana je odabrana za `timA` i zato je više nema na listi `igraci`.