## Odd players

Let's improve your program to work with an odd number of players.



+ Add another name to your `players.txt` list, so that you have an odd number of players.

	![screenshot](images/team-luna.png)

+ If you test your code, you'll see that you get an error message.

	![screenshot](images/team-error.png)

+ The error is because your program keeps choosing random players for team A and then team B. However, if there is an odd number of players then after choosing a player for team A there are no players left to choose from for team B.

	To fix this bug, you can tell your program to `break` out of your `while` loop if your `players` list is empty.

	![screenshot](images/team-fix.png)

+ If you test your code again, you should see that it now works with an odd number of players.

	![screenshot](images/team-fix-test.png)



