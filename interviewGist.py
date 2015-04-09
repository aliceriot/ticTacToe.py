#!/usr/bin/python

## A class which gives us a board and all the methods we need to work with it

class Board:
    def __init__(self):
        self.board = {1:" ",
                2:" ",
                3:" ",
                4:" ",
                5:" ",
                6:" ",
                7:" ",
                8:" ",
                9:" "}
        self.complete = False

    def winningMove(self):
        """
        check board for any winning moves
        """
        if self.board[1] == self.board[2] == self.board[3] and self.board[1] != ' ':
            return (True, self.board[1])
        elif self.board[4] == self.board[5] == self.board[6] and self.board[4] != ' ':
            return (True, self.board[4])
        elif self.board[7] == self.board[8] == self.board[9] and self.board[7] != ' ':
            return (True, self.board[7])
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ':
            return (True, self.board[1])
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ':
            return (True, self.board[2])
        elif self.board[3] == self.board[6] == self.board[9] and self.board[3] != ' ':
            return (True, self.board[3])
        elif self.board[1] == self.board[5] == self.board[9] and self.board[1] != ' ':
            return (True, self.board[1])
        elif self.board[3] == self.board[5] == self.board[7] and self.board[3] != ' ':
            return (True, self.board[3])
        else:
            return (False, '')

    def displayBoard(self):
        """
        just prints out the board
        """
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
 
    def gameOver(self):
        """
        work with winning move state to determine when to end game
        """
        state = self.winningMove()
        if state[0] == False:
            if ' ' not in self.board.values():
                return True
            else:
                return False
        else:
            return True

    def tryMove(self, move):
        """
        try out moves to see if valid
        """
        if move not in range(1,10):
            return False
        elif self.board[move] != ' ':
            return False
        else:
            return True
        

gameBoard = Board()

print("Welcome to tic-tac-toe!")

gameBoard.displayBoard()

while not gameBoard.gameOver():

    #X's turn
    notMovedYetX = True
    while notMovedYetX:
        try:
            move = int(input("X, Make a move! 1-9 "))
        except:
            move = 0
        if gameBoard.tryMove(move):
            gameBoard.board[move] = 'X'
            notMovedYetX = False
        else:
            print("No good, pick better!")

    gameBoard.displayBoard()

    if gameBoard.gameOver():
        state = gameBoard.winningMove()
        if state[0]:
            print("The winner is " + state[1])
        else:
            print("It's a draw!")
        break

    #O's turn
    notMovedYetO = True
    while notMovedYetO:
        try:
            move = int(input("O, Make a move! 1-9 "))
        except:
            move = 0
        if gameBoard.tryMove(move):
            gameBoard.board[move] = 'O'
            notMovedYetO = False
        else:
            print("No good, pick better!")
            
    gameBoard.displayBoard()

    if gameBoard.gameOver():
        state = gameBoard.winningMove()
        if state[0]:
            print("The winner is " + state[1])
        else:
            print("It's a draw!")
        break

    gameBoard.displayBoard()





