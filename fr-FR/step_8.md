## Joueurs impair

Essayons d'améliorer notre programme pour qu'il fonctionne avec une listes de joueurs impair.

+ Ajoute un autre nom a ta liste `players.txt`, pour que tu ais une liste impair de joueurs.

	![screenshot](images/team-luna.png)

+ Si tu test ton code, tu devrais voir une erreur s'afficher.

	![screenshot](images/team-error.png)

+ Cette erreur s'affiche parce que ton programme continue de choisir des joueurs aléatoire de l'équipe A et B. Sauf que maintenant, si il y a un nombre impair de joueurs alors après avoir choisi un joueur pour l'équipe A, il n'y a plus de joueurs disponible pour léquipe B.

	Pour corriger ce probléme, tu peux dire à ton programme de stopper (ou `break`) ta boucle `while` si ta liste de joueurs `players` est vide. 

	![screenshot](images/team-fix.png)

+ Si tu test ton code encore une fois, tu devrais avoir que cela fonctionne avec un nombre impair de joueurs.

	![screenshot](images/team-fix-test.png)



