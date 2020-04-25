# 14PuzzleProblem
Graph Search algorithm with A* Search Strategy for solving the 14-puzzle problem


## 14-puzzle problem: 
On a 4 x 4 board there are 14 tiles numbered from 1 to 14 and two blank positions. A tile can slide into any of the two blank positions if it is horizontally or vertically adjacent to the blank position. Given a start board configuration and a goal board configuration, find a sequence of moves to reach the goal configuration from the start configuration. The goal is to find a solution with minimum number of moves.

## Input and output file format: 
The program reads in the initial and goal states from a text file that contains nine lines as shown below.
__________________________________________________________________________________________________________________
n n n n
n n n n
n n n n
n n n n

m m m m
m m m m
m m m m
m m m m
_________________________________________________________________________________________________________________


Lines 1 to 4 contain the tile pattern for the initial state and lines 6 to 9 contain the tile pattern for the goal state. Line 5 is a blank line. n and m are integers that range from 0 to 14. Integer 0 represents a blank position and integers 1 to 14 represent tile numbers. 

The program produces an output text file that contains 13 14 lines as shown in Figure 2 below:
____________________________________________________________________________________________________________________
n n n n
n n n n
n n n n
n n n n

m m m m
m m m m
m m m m
m m m m

d
N
A A A A A A....
ffffff.....
____________________________________________________________________________________________________________________

Lines 1 to 4 and lines 6 to 9 contain the tile patterns for the initial and goal states as given in the input file. Lines 5 and 10 are blank lines. Line 11 is the depth level d of the shallowest goal node as found by your search algorithm (assume the root node is at level 0.) Line 12 is the total number of nodes N generated in the tree (including the root node.) Line 13 contains the solution that is found. 

The solution is a sequence of actions (from root node to goal node) represented by the A’s in line 13. Each A is a character from the set {L1, R1, U1, D1, L2, R2, U2, D2}, which represents the left, right, up and down movements of the two blank positions. Line 14 contains the f(n) values of the nodes along the solution path, from root node to the goal node. There should be d number of A values in line 13 and d+1 number of f values in line 14.

# Test your file
To change the input file name, go to main function in 14puzzle.py and change the in_file variable to the whatever file name you want to put

# How to run?
Go to the 14puzzle.py directory in the terminal
n terminal, run `python 14puzzle.py`
