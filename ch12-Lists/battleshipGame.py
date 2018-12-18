from battleshipUtilities import *

def main():
    # Create empty board
    print("Creating game board...")
    board = Board()
    board.createGameBoard()

    # Place battleships randomly
    board.placeBattleships()
    #board.printBoardDebug()
    print(board.shipLocations)

    # Game loop
    while board.shipsRemaining > 0:
        board.printBoard()
        inputCell = input("Enter a game cell to shoot at (A1-C4): ")
        print("You entered " + inputCell)
        break

if __name__ == "__main__":
    main()