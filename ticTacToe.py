
#this defines a class with all the methods we need for the 
#tic tac toe game

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


        

