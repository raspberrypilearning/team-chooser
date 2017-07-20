--- challenge ---
## Challenge: Adding more players
Can you add more players to your list? You can add as many players as you like, but make sure that there is an __even__ number of players.

You can also change the names of the first 2 players if you prefer.

Can you add code to print __just one__ of your new players?



## Step 2: Random players

Let's choose random players!



+ To be able to get a random player from your `players` list, first you'll need to import the `choice` part of the `random` module.

	![screenshot](images/team-import-random.png)

+ To get a random player, you can use `choice`. (You can also delete the code to print individual players.)

	![screenshot](images/team-random-player.png)

+ Test your `choice` code a few times and you should see a different player being chosen each time.

+ You can also create a new variable called `playerA`, and use it to store your random player.

	![screenshot](images/team-random-playerA.png)

+ You'll need a new list to store all of the players in team A. To start with, this list should be empty.

	![screenshot](images/team-teamA.png)

+ You can now add your randomly chosen player to `teamA`. To do this, you can use `teamA.append` (__append__ means add to the end).

	![screenshot](images/team-teamA-add.png)

+ Now that your player has been chosen, you can remove them from your list of `players`.

	![screenshot](images/team-players-remove.png)

+ Test this code by adding a `print` command, to show the `players` left to choose from.

	![screenshot](images/team-players-remove-test.png)

	In the example above, Hermione has been chosen for `teamA`, and so has been removed from the list of `players`.




--- /challenge ---### Additional information for club leaders

If you need to print this project, please use the [Printer friendly version](https://projects.raspberry-pi.org/en/projects/team-chooser/print).


--- collapse ---
---
title: Club leader notes
---


## Introduction:
In this project, children will learn how to make a program to split a list of players into 2 random teams. This project teaches lists and using files.

## Online Resources

__This project uses Python 3.__ We recommend using [trinket](https://trinket.io/) to write Python online. This project contains the following Trinkets:

+ [New (blank) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

There is also a trinket containing the completed project:

+ [‘Team Chooser’ Finished -- trinket.io/python/a699c44ce6](https://trinket.io/python/a699c44ce6)

## Offline Resources
This project can be [completed offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) if preferred. You can access the project resources by clicking the 'Project Materials' link for this project. This link contains a 'Project Resources' section, which includes resources that children will need to complete this project offline. Make sure that each child has access to a copy of these resources. This section includes the following files:

+ team/team.py

You can also find a completed version of this project in the 'Volunteer Resources' section, which contains:

+ team-finished/team.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

## Learning Objectives
+ Lists;
+ Loading list data from a file.

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

+ [Use basic programming constructs to create simple programs.](https://www.raspberrypi.org/curriculum/programming/creator)

## Challenges
+ "Adding more players" - adding elements to a `players` list;
+ "Choosing for team B" - creating a new `teamB` list to add random players to;
+ "Random team names" - creating and using a new `teamNames` list to assign random names to teams;
+ "Storing team names" - storing team names in a file, and loading them into a `teamNames` variable;
+ "More teams" - splitting players into 3 teams instead of 2.

--- /collapse ---


--- collapse ---
---
title: Project materials
---
## Project resources
* [.zip file containing all project resources](resources/team-chooser-project-resources.zip)
* [Online blank Python Trinket](http://jumpto.cc/python-new)
* [Offline blank Python file](resources/new-new.py)

## Club leader resources
* [.zip file containing all completed project resources](resources/team-chooser-volunteer-resources.zip)
* [Online completed Trinket project](https://trinket.io/python/a699c44ce6)
* [team-chooser-finished/team-chooser.py](resources/team-chooser-finished-team-chooser.py)

--- /collapse ---