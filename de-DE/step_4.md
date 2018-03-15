## Beliebige Mitspieler

Lass uns beliebige Mitspieler wählen!

+ Um in der Lage zu sein, einen beliebigen Mitspieler von deiner `players` Liste (Mitspielerliste) aufzurufen, musst du zuerst den `choice` (Wahl) Teil des `random` (beliebig) Moduls importieren.

	![screenshot](images/team-import-random.png)

+ Um einen beliebigen Mitspieler aufzurufen, kannst du `choice` (Wahl) benutzen. (Du kannst den Code auch löschen, um einzelne Mitspieler auszudrucken.)

	![screenshot](images/team-random-player.png)

+ Teste deinen `choice` (Wahl) Code ein paar Mal und du kannst dann sehen, wie jedes Mal ein anderer Mitspieler ausgewählt wird.

+ Du kannst auch eine neue Variable namens `playerA` (Spieler A) erstellen und diese dazu benutzen, deinen beliebigen Spieler zu speichern.

	![screenshot](images/team-random-playerA.png)

+ Du brauchst eine neue Liste, um alle Mitspieler in Team A zu speichern. Zu Beginn sollte diese Liste jedoch leer sein.

	![screenshot](images/team-teamA.png)

+ Du kannst jetzt deinen beliebig ausgewählten Mitspieler dem `teamA` hinzufügen. Um dies zu tun, kannst du `teamA.append` benutzen (__append __ heißt wörtlich: „anfügen“ und bedeutet, etwas dem Ende hinzufügen).

	![screenshot](images/team-teamA-add.png)

+ Jetzt, wo du deinen Mitspieler ausgewählt hast, kannst du ihn von der Liste an `players` (Mitspielern) entfernen.

	![screenshot](images/team-players-remove.png)

+ Teste diesen Code, indem du einen `print` (drucken) Befehl hinzufügst, um die verbleibenden `players` (Mitspieler) anzuzeigen, unter denen du noch auswählen kannst.

	![screenshot](images/team-players-remove-test.png)

	In dem o.g. Beispiel wurde Hermione für `teamA` ausgewählt und wurde daher von der Liste der `players` (Mitspieler) entfernt.
