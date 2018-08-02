from queue import *
        
def main():
    loop = True
    queue = []
    userInput = ""

    while loop:
        userInput = input("Enter a value to be input into a queue, \"?\" to \
pop a value off the queue, or press \"Enter\" to exit the program: ")
        if not userInput:
            break
        elif userInput == "?":
            poppedValue = pop(queue)
            if poppedValue: print(poppedValue)
        else:
            queue.append(userInput)

    print("Exiting program...")
    return

if __name__ == "__main__":
    main()