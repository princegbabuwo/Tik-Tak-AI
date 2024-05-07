# Tik-Tak-AI

In this TikTak AI, We want to design an AI player that plays a Tic Tac Toe Game with a human player.

First what is a Tic Tac Toe Game

[Add Image]

A Tic Tac Toe game is a game in which two players play with the objective of being the first player to get three of their marks(X or O) in a horizontal, vertical, or diagonal row.

1. Tic Tac Toe game consist of a 3x3 grid.
2. The player to play first is decided randomly(and in this code, both the human player and the AI player would be given a 50/50 chance of playing first.)
3. Players take turn marking empty grids with their respective symbols(X or O)
4. The defualt symbol for the AI player in this game is 'X' while the symbol for the human player is 'O'
5. A player wins if they create a row of three Xs or Os (horizontally, vertially, or diagonally)

[3 Images of possible wins]

(Definition Courtesy: Google Gemini)

For our AI player, we shall define some heuristics sets of rules that would guide the AI player in making its strategy decisions.

Primarily, our AI player is interested in two events, which are:
1. Winning the game
2. Making sure the opponent does not win the game

The heuristic rules for the AI player will assign some utility values to each grid in the tic tac toe game based on the possibilities of the above mentioned events and the AI player will make its decision on its next move based on these assigned values.

First let's represent each grid in the tic tac toe game with a respective number.

[1, 2, 3]

[4, 5, 6]

[7, 8, 9]

(use an matrix image to represent this)

Now let's consider the stage states of winning the game. The possible stage states of winning the game are:

[1, 2, 3] <- Horizontal Victory

[4, 5, 6] <- Horizontal Victory

[7, 8, 9] <- Horizontal Victory

[1, 4, 7] <- Vertical Victory

[2, 5, 8] <- Vertical Victory

[3, 6, 9] <- Vertical Victory

[1, 5, 9] <- Diagonal Victory

[3, 5, 7] <- Diagonal Victory

Before the A.I player makes it moves, we shall explore the possible winning stage space of the game and add a utility value to each grid in the game using the following rules below:

1. Before the AI player makes its next move, we shall first initilize the grids with a utility value of 0 to all empty grids and a utility value of -1 to all filled grids.

2. Next, we shall add a utility value of 1000 to to an empty grid if the other two grids in a possible winning stage space are already filled in by the A.I. 

    This would be the highest utility value we would add to a grid as winning the game is the topmost priority of our AI player
2. We shall add a utility value of 100 to an empty grid if the other two grids in a possible winning stage space are already filled in by the human player.
    
    This would be the second highest utility value we would add to an empty grid as the second priority of our AI player is to ensure the human player does not win the game.
3. We would add a utility value of 10 to the empty grids in a possible winning stage space if the AI player has filled in one and only one grid in the stage state and the other grids in the possible winning stage states are empty.

    This stage space is one that can help the AI player in building a winning path hence a utility value of 10 is added.
4. We will not add any utility value to a empty grids in a possible winning stage space if we have atmost one grid in the stage space that was filled in by the human player.

    This stage space is not intresting to A.I player as a winning path cannot be built from such a stage space hence no value is added.
5. We would add a utility value of 1 to all the grids in a possible winning stage space if all the grids in the stage space are empty 
7. When adding a utility value to an empty grid, the newly added utility value will be summed with the previously added utility value of that grid

After all the utility values has been added to each grids in the game, the AI player will make its next move by playing in the grid with the highest utility value.

If there are more than one grid with the highest utility value, the AI player would play randomly in one of those grids.

Let's consider some gaming scenarious.

First Let's consider the scenario where the AI player plays first.

[. . .]

[. . .]

[. . .]

From our above rueles,
All grids are empty and so would be initialized to 0.

[0 0 0]

[0 0 0]

[0 0 0]

Considering the possible winning stage space: [1, 2, 3]

Since all the grids are empty, Rule 5, would be followed, therefore we have our updated utility values to be:

[1 1 1]

[0 0 0]

[0 0 0]

Similarly, for the stage spaces: [4, 5, 6] an [7, 8, 9]: Our utility values will be updated to:

[1 1 1]

[1 1 1]

[1 1 1]

Again, considering the possible winning combinations of: [1, 4, 7] & [2, 5, 8] & [3, 6, 9]: Our utility values would be updated to:

[2 2 2]

[2 2 2]

[2 2 2]

Considering the diagonal winning combination [1, 5, 9], our utility values would be updated to

[3 2 2]

[2 3 2]

[2 2 3]

Lastly, for the diangonal winning combination [3, 5, 7], our utility values would be updated to

[3 2 3]

[2 4 2]

[3 2 3]

Therefore according to our heuristic rules, the AI player would always start from the middle(Grid-5) when it to play first.

The ulity values will keep being updated for the AI player as the human player makes it next moves until the game ends in a win, draw or lose for the AI player.

According to www.half-real.net/tictactoe 

There are 255,168 possible unique games of tic tac to that can be played of which:

131,184 are won by the first player, 

77,904 are won by the second player, 

and 46,080 are drawn.

However, after using a Depth-First-Search algorithm on the Heuristic guidance for the A.I player, we were able to deduce the following:

There is a total of 2,240 unique games that can be played between the Human and AI player

of which only 120 games can be won by human 

1776 can be won by the AI player

and a the game can end in a draw only 344 times

The more interesting part is that is that: When the AI player makes the first move, only 248 unique games can be played;

of which 224 would be won be the AI player, 24 of the unique games would result into a draw and the human player does not get to win any of this games.

From the above illustration, we have seen how the Heuristic guided AI player has become intelligent and has avoided alot of unintelligent moves thereby reducing the total games than can be played with the human player from 255,168 to a mere 2,240 games of which 1,776 (79%) of the unique games would be won by the AI player.

In constrast, assuming the AI player plays randonmly, both the Human player and the AI player would have equal chances of winning the game but in reality, the human player would tend to win more as the human player would be much smarter than an AI player who plays at random

The function `gameCounts()` for counting the game is in the main.py script: 

To get started:

clone the code at https://github.com/princegbabuwo/Tik-Tak-AI.git

Open a terminal at the cloned folder and enther the following prompts

    >cd tik-tak-ai
    
    >py main.py

