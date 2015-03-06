#!/usr/bin/python

import ticTacToe

gameBoard = ticTacToe.Board()

print("Welcome to tic-tac-toe!")

gameBoard.displayBoard()

while not gameBoard.gameOver():

    #X's turn
    notMovedYetX = True
    while notMovedYetX:
        move = int(input("X, Make a move! 1-9 "))
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
        move = int(input("O, Make a move! 1-9 "))
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





