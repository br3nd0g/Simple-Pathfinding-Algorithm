# Pathfinding Algorithm

This is a simple python program which generates a "board" of ascii characters, asks the user for a percentage to move along and down in percentages (e.g. 100% x-axis 100% y-axis). It also asks the user for an amount of obstacles to generate, which the algorithm pathfinds around.

Variables like the board size and obstacle size are variables which can easily be tweaked with no detriment to the program. The program is slow, and unreliable though, as it runs in the terminal.

## Things to be improved upon 

There are some things *currently* unaccounted for such as the fact that if the goal the user specifies ends up being somewhere where an obstacle is placed, it will not be able to reach the goal. I have also not tested this case, so it could cause an error perhaps.