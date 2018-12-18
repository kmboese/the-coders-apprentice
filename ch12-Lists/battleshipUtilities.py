from random import randint

class Board:
    # Create a gameboard (3x4 by default)
    def __init__(self, rows=3, cols=4, ships=3):
        self.rows = rows
        self.cols = cols
        self.gameBoard = []
        # Locations of the placed battleships
        self.shipLocations = []
        self.shipsRemaining = ships

    # Creates a game board for battleship (3x4 by default)
    def createGameBoard(self):
        for i in range(self.rows):
            row = ["."]*self.cols
            self.gameBoard.append(row)

    # Randomly place @ships battleships on the board
    def placeBattleships(self, ships=3):
        for i in range(ships):
            index = randint(0,ships)
            self.gameBoard[i][index] = "X"
            # Save the battleship location as a grid tuple
            self.shipLocations.append((chr(ord("A") + i), index+1))

    # Prints the board with the battleships marked
    def printBoardDebug(self):
        rowLetter = "A"
        colLetter = 1
        print("\nGame board (debug):")

        # Print column headers
        print("{:5}".format(" "),end='')
        for i in range(self.cols):
            print("{}{:3}".format(i+1, " "),end='')
        print()

        for row in self.gameBoard:
            print("{} {:3}".format(rowLetter, "["), end='')
            for cell in row:
                print("{:3} ".format(cell), end='')
            print("]")
            rowLetter = chr(ord(rowLetter) + 1)
        print()

    # Print the board showing only hits, misses, or empty cells
    def printBoard(self):
        rowLetter = "A"
        colLetter = 1
        contents = None
        print("\nGame board:")

        # Print column headers
        print("{:5}".format(" "),end='')
        for i in range(self.cols):
            print("{}{:3}".format(i+1, " "),end='')
        print()

        for row in self.gameBoard:
            print("{} {:3}".format(rowLetter, "["), end='')
            for cell in row:
                if cell == "X":
                    contents = "."
                else:
                    contents = cell
                print("{:3} ".format(contents), end='')


            print("]")
            rowLetter = chr(ord(rowLetter) + 1)
        print()