## Ungleiche Anzahl an Mitspielern

Lass uns dein Programm verbessern, um mit einer ungleichen Anzahl von Mitspielern zu arbeiten.

 + Füge einen weiteren Namen zu deiner `players.txt` Liste (Mitspielerliste) hinzu, sodass du eine ungleiche Anzahl an Mitspielern hast.

	![screenshot](images/team-luna.png)

+ Wenn du deinen Code testest, wirst du sehen, dass du eine Fehlermeldung erhältst.

	![screenshot](images/team-error.png)

+ Dieser Fehler liegt daran, dass dein Programm weiterhin beliebige Mitspieler für Team A und dann Team B auswählt. Wenn es jedoch eine ungleiche Anzahl an Mitspielern geben sollte, dann wird es nach der Wahl eines Mitspielers für Team A keine weiteren Mitspieler für Team B geben, die gewählt werden können.

	Um diesen Fehler zu beheben , kannst du deinem Programm mitteilen, dass es aus deiner `while` (Weileschleife) `break` (ausbrechen) soll, wenn deine `players` Liste (Mitspielerliste) leer ist. 

	![screenshot](images/team-fix.png)

+ Wenn du dann wieder deinen Code testest, solltest du jetzt sehen können, dass er mit einer ungeraden Zahl an Mitspielern funktioniert.

	![screenshot](images/team-fix-test.png)



