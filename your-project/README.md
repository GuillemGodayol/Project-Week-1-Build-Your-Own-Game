<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Soldiers & Dice
*Guillem Godayol*

*[Data Analytics, Barcelona & 10/2019]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
The project consists in a Risk battle, with some soldiers defending a territory and others attacking it. The result of this battle is evaluated by dice rolls. I chose this game because I've played many times at Risk.

## Rules
One player is the Defending team, who wants to keep his territory.
Other player is the Attacking team, who wants to conquer a new territory.
The Attacking team must attack with more than 1 soldier, as he can't leave his own territory unoccupied.
After the rolls, the player with more alive soldiers wins the battle, and keeps or wins the territory.

## Workflow
I organized the code in two sections. The first one is where I define all the functions needed. The second one is the code for the game itself.

The process starts asking for the number of soldiers for each player, and checking if this number fits into the requirements.

After that, the game asks each player how many dice should would like to roll. The function at this point also checks if there is any specific condition that don't allows the player to choose.

Once we have the number of dices, the 'random' function assigns random values to each one.

And after that, it's time to check the maximum of each player's roll and compare. Somebody will loose a soldier! If there are enough dices, the operation its done again. Due to game rules, it can only be done twice.

Now it's time to print the loses for each player and make an update of the number of soldiers. If, according to the rules, there are enough soldiers, the game asks again for the number of dices to be rolled.

If there are no enough soldiers in any of the two players, the game ends.

## Organization
To get organized I used Trello, with 3 columns: Steps, Work in Progress, Finished.
It helped me to know the pending steps and to decide when to hurry.

<img src="https://github.com/GuillemGodayol/Project-Week-1-Build-Your-Own-Game/blob/master/pictures/Kanban%20Screenshot.png" alt="Trello screenshot" width="800"/>

The repository is quite simple: 
one folder named 'pictures', where you can find a picture of my Kanban in Trello
one folder named 'your-project', where you can find this readme.md file, the code (named 'soldiers_&_dice') and the pseudocode.md

## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/GuillemGodayol/Project-Week-1-Build-Your-Own-Game)  
[Slides](https://docs.google.com/presentation/d/1f72U4SY5-3CgZkUNhL2g0DEi7R8eKOEL1Wk3FORlM8s/edit?usp=sharing)  
 
