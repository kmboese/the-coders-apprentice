# Range of cells in the maze
LOWEST_CELL = 1
HIGHEST_CELL = 16

def connected( x, y ):
    if x > y:
        return connected( y, x )
    if (x,y) in ((1,5),(2,3),(3,7),(4,8),(5,6),(5,9),(6,7),
        (8,12),(9,10),(9,13),(10,11),(10,14),(11,12),(11,15),
        (15,16)):
        return True
    return False

def edges(x):
    return ([i for i in range(LOWEST_CELL, HIGHEST_CELL+1) if connected(x,i)])
    
def entrance():
    return LOWEST_CELL
    
def exit():
    return HIGHEST_CELL

def findPathToExit(current=entrance(), cellList=[], visitedList=[]):

    if current == entrance():
        visitedList.append(current)

    # Base case: we found the exit
    if (current == exit()):
        return True
    
    # DFS path finding
    for cell in edges(current):
        if cell not in visitedList:
            visitedList.append(cell)
            if findPathToExit(cell, cellList, visitedList) and connected(current,cell):
                cellList.append(cell)
                # Special case: append the entrance on the last recursive step and return the list
                if (connected(cell, entrance())):
                    cellList.append(entrance())
                    return cellList, visitedList
                return cell


def main():
    path, visitedList = findPathToExit()
    print("Finding path...\nPath to exit is {}".format(path))
    print("Cells visited: {}".format(visitedList))

if __name__ == "__main__":
    main()