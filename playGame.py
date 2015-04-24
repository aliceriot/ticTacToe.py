#!/usr/bin/python

import ticTacToe

gameBoard = ticTacToe.Board()

print("Welcome to tic-tac-toe!")

gameBoard.displayBoard()

computerChoice = input("Would you like to play a computer? (y/n)")
    
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

    if computerChoice == 'y':
        move = gameBoard.computerMove()
        gameBoard.board[move] = 'O'

    else: #play interaction
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





