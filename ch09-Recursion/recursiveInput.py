# This code is incredibly bad. Fix it by adding a function "getInputFixed()".
def getInput(prompt):
    value = input(prompt)
    for letter in value:
        if letter < 'a' or letter > 'z':
            print("The character \'{}\' is not allowed!".format(letter))
            value = getInput(prompt) # DO NOT DO THIS
    return value

# This code is still ugly but at least it works
def getInputFixed(prompt):
    value = input(prompt)
    for letter in value:
        if letter < 'a' or letter > 'z':
            print("The character \'{}\' is not allowed!".format(letter))
            # This is still a crazy way to get user input, but the return
            # statement means that the current for loop is terminated on 
            # iteration, thus preventing the nested prompts the other code
            # gives.
            return(getInputFixed(prompt))  
    return value


def main():
    #s = getInput("Give a string of lower case letters: ")
    s = getInputFixed("Give a string of lower case letters: ")
    print("The user entered: {}".format(s))

if __name__ == "__main__":
    main()