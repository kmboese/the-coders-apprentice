# Constants
ALPHABET_SIZE = 26

def isLetter(char):
    return char.lower() >= 'a' and char.lower() <= 'z'

# Return the index of a letter relative to the letter 'a' in ASCII
# 'a' == 0, 'z' == 25
def indexLetter(char):
    return(ord(char)-ord('a'))
        
def countLetterFrequency(string):
    frequencies = [("",0)]*ALPHABET_SIZE

    lowerString = string.lower()
    for char in lowerString:
        if isLetter(char):
            count = frequencies[indexLetter(char)][1] + 1
            frequencies[indexLetter(char)] = (char, count)

    return frequencies

def printFrequencies(frequencies):
    frequencies.sort(key=lambda frequency: frequency[1], reverse=True)
    for i in range(len(frequencies)):
        if (i != 0 and i%7 == 0):
            print()
        # Only print characters that appeared at least once
        if frequencies[i][1] > 0:
            print("{}".format(frequencies[i]), end='     ')