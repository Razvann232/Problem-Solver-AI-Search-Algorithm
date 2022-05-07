# Problem-Solver-AI-Search-Algorithm
Implementing a program that generates solutions for a classic problem using search algorithms (+ visual representation).

A classic river-crossing logic puzzle known as the "missionaires and cannibals problem" is solved using artificial inteligence (more specifically search algorithms).

***PyGame package is required for the application to work.***

The problem:
A given number of cannibals and missionaries must cross a river with a boat that can transport a given number of persons. The two groups and the boat are on the same side of the river and must successfully cross to the other side, however if at any time on any side of the river there are more cannibals than missionaries the cannibals will eat the missionaries. The solution found must be the most efficient (as few boat movements as possible).

More info on the problem can be found here: https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

The problem is solved using search algorithms:
1. Depth First Search (DFS)
2. Breadth First Search (BFS)
3. A-star algorithm (A*)
4. Uniform Cost Search

Three scenarios can be used for each algorithm depending on the difficulty (number of people in each group). 
A helpful UI and a visual animation are used to display the solution. The number of individuals on each side will
be represented by an 'x No' underneath their icons.

The 'main' method in the 'main' class must be run for the program to start.
