PUNCTUATION = [",", ".", "!", "?", "..."]
DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday",\
    "saturday"]

def isCaps(char):
    return (char >= "A" and char <= "Z")

def isLower(char):
    return (char >= "a" and char <= "z")

def isLetter(char):
    return (isCaps(char) or isLower(char))

def capitalizeDays(stringList):
    ret = []
    for s in stringList:
        if s.strip().strip(",").lower() in DAYS:
            print("{} is a day of the week".format(s))
            if isLower(s[0]):
                tmp = s[0].upper() + s[1:]
                ret.append(tmp)
        else:
            ret.append(s)
    return ret


#Capitalize the first word of a sentence if it is an alpha character
def capitalize(stringList):
    ret = []
    if stringList:
        firstWord = stringList[0]
        if isLetter(firstWord[0]):
            if len(firstWord) > 1:
                tmp = firstWord[0].upper() + firstWord[1:]
            else:
                tmp = firstWord[0].upper()
            ret.append(tmp)
    ret.extend(stringList[1:])
    return ret


# change all consecutive double upper case letters to single uppercase and 
# single lowercase (i.e. "HEllo" becomes "Hello") and invert cAPS mISTAKES.
def fixCaps(stringList):
    ret = []
    for s in stringList:
        changed = False
        if len(s) < 2:
            ret.append(s)
            continue
        # If there are two consecutive caps at the beginning of a word, turn 
        # the second one into a lowercase letter.
        if (isCaps(s[0]) and isCaps(s[1])):
            if len(s) > 2:
                ret.append(s[0] + s[1].lower() + s[2:])
            # string is exactly two characters long
            else:
                ret.append(s[0] + s[1].lower())
        # Correct caps lock mistakes
        elif isLower(s[0]) and s[1:] == s[1:].upper():
            ret.append(s[0].upper() + s[1:].lower())
        # Otherwise, make no changes and append the string as-is
        else:
            ret.append(s)
    return ret


# Remove a string if its immediate successor is the same string
def removeImmediateDuplicates(stringList):
    changed = None
    ret = []
    for i in range(0, len(stringList)-1):
        changed = False
        # Check if the strings are the same except for one puncuation mark
        # at the end.
        for punc in PUNCTUATION: 
            if stringList[i].split(punc)[0] == \
                stringList[i+1].split(punc)[0]:
                changed = True
                break
        # If adjacent strings are identical, remove one of them
        if not changed and stringList[i] != stringList[i+1]:
            ret.append(stringList[i] + " ")
            continue
    ret.append(stringList[len(stringList)-1])
    return ret


def correctString(s):
    ret = ""
    substrings = s.split()
    capitalized = capitalize(substrings)
    fixedCaps = fixCaps(capitalized)
    noDupes = removeImmediateDuplicates(fixedCaps)
    capitalizedDays = capitalizeDays(noDupes)

    for s in capitalizedDays:
        ret += s
    print("Corrected string: {}".format(ret))
    return ret

def main():
    #s = "hello there KEvin, gOOD sir sir. Great saturday, huh?"
    s = '''as it turned out our change meeting with REverend \
aRTHUR BElling was was to change our whole way of life, and \
every sunday we'd hurry along to St 100NY up the Cream BUn \
and Jam...'''
    print("Original string: {}".format(s))
    corrected = correctString(s)

if __name__ == "__main__":
    main()