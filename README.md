# Tic-Tac-Toe
Tic Tac Toe implementaion, Written in Python 3 with PyQt5 GUI.

In this Tic Tac To implementaion the user play against the computer, To display the game board we designed a user friendly GUI that displays the game board at any time Given, our game starts with the user having to select the sign with which he wants to play (X or O),  Who takes the first turn is randomly chosen, Then the player and computer take turns making moves. we also defined several variables: **playerSymbol** keeps the mark with which the player plays, **computerSymbol** keeps the mark which the computer playing, **myTable** is an array of String with the size of 9, which at any given time keeps the player's and computer's position, in fact The array positions represent the game panel and this can be described by the following example:

<p align="center"> 
<img src="https://user-images.githubusercontent.com/31032862/57181593-7c407d00-6e9e-11e9-8576-5a51f706c717.png" width="50%">
</p>

We have defined the **chooseSymbol()** method which allows the player to choose which sign he Wants to play with, the method also randomly decides who will start the game. The player chooses The desired square by clicking it on the game screen and the method responsible for it is **choosenPosition()** which marks the player's sign in the desired square and updates myTable array Where desired. The main method used for the computer turn is **ComputerTurn()**, When the method is activated it first checks to see if there is a free square that can bring the computer to victory, this is done by copying myTable to a temporary array and check by a loop in all the squares, if such a square is found It returned, otherwise check whether there is a square that the player can win with in his next turn, if there is such a square it is returned.

After each move of the player or computer two methods applayed, the first is **findWinner()** Which checks in myTable array whether there is a Vertical, horizontal or diagonal row filled with the same mark and if so does notify On a win, for example if myTable[1] & myTable[5] & myTable[9] with the same sign then that means that the diagonal is full, the second method that is activated is **checkForTie()**, it checks whether the myTable array is full, if it is it means that the game is finished in a tie.


Application GUI and implementation:
-

**The Game menu screen:**
<p align="center"> 
<img src="https://user-images.githubusercontent.com/31032862/57181920-3b4a6780-6ea2-11e9-8008-1536f92d268d.png" width="50%">
</p>

**choosen symbol screen:**
<p align="center"> 
<img src="https://user-images.githubusercontent.com/31032862/57181924-4bfadd80-6ea2-11e9-9906-3ab5c40ab482.png" width="50%">
</p>

**Game Over scree, the computer has won:**
<p align="center"> 
<img src="https://user-images.githubusercontent.com/31032862/57181928-574e0900-6ea2-11e9-92ce-b1441bd2fc99.png" width="50%">
</p>
