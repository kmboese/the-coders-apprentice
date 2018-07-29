import re
PUNCTUATION = [",", ".", "!", "?", "..."]
DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday",\
    "saturday"]

def isUpper(char):
    return (char >= "A" and char <= "Z")

def isLower(char):
    return (char >= "a" and char <= "z")

def isLetter(char):
    return (isUpper(char) or isLower(char))

# Split a string into tokens based on whitespace and 
# punctuation.
def tokenize(s):
    tokens = []
    # Split based on any non-word string
    tokens = re.split(r'(\W+)', s)
    return tokens

# Remove double caps from a word (i.e. "HEllo"-->"Hello")
def removeDoubleCaps(s):
    ret = ""
    if len(s) < 2:
        return s
    else:
        if isUpper(s[0]) and isUpper(s[1]):
            if len(s) == 2:
                ret = s[0] + s[1].lower()
            else:
                ret = s[0] + s[1].lower() + s[2:]
            return ret
        else:
            return s

# Returns an empty string if a duplicate is detected
def isDuplicate(s1, s2):
    if s1.lower() == s2.lower():
        return True
    else:
        return False

# Check if a word is a day of the week
def isDayOfWeek(s):
    return (s.lower() in DAYS)

# Check if a word has double caps
def hasDoubleCaps(s):
    if len(s) <= 1:
        return False
    elif len(s) >= 2 and isUpper(s[0]) and isUpper(s[1]):
        return True
    else:
        return False
# Check if a word has cAPS cASING
def hasCapsCasing(s):
    if len(s) < 2:
        return False
    elif len(s) >=2 and isLower(s[0]) and isUpper(s[1]):
        return True

# Fix caps casing
def fixCapsCasing(s):
    return s[0].upper() + s[1:].lower()

# Capitalize the first word of a sentence
def capitalizeFirstWord(string):
    if len(string) == 1:
        return string[0].upper()
    else:
        return string[0].upper() + string[1:]

def correctSentence(s):
    ret = ""
    tokens = tokenize(s)
    duplicateRemoved = False

    # Correct strings in the sentence
    for i in range(0, len(tokens)-1):
        # Only correct words that are at least one character 
        # and start with a letter
        if len(tokens[i]) >= 1 and isLetter(tokens[i][0]):
            # If a duplicate pair is found, skip the current string to remove
            # the duplicate.
            if isDuplicate(tokens[i], tokens[i+2]):
                duplicateRemoved = True
                continue

            # If the first word start with a lowercase letter, capitalize it
            elif i == 0 and isLower(tokens[0][0]):
                ret += capitalizeFirstWord(tokens[0])
                continue

            # If the word has DOuble CAps, remove the second caps letter
            elif hasDoubleCaps(tokens[i]):
                ret += removeDoubleCaps(tokens[i])
                continue

            # If the word has cAPS cASING, fix it
            elif hasCapsCasing(tokens[i]):
                ret += fixCapsCasing(tokens[i])
                continue

            # If the word is a day of the week and lowercase, make it 
            # uppercase
            elif isDayOfWeek(tokens[i]):
                ret += tokens[i][0].upper() + tokens[i][1:]
                continue

            # Default: add the token to the string
            else:
                ret += tokens[i]
            
        # Non-word string
        else:
            # Remove the trailing whitespace after a string is removed
            if tokens[i] == " " and duplicateRemoved:
                duplicateRemoved = False
                continue
            else:
                ret += tokens[i]

    return ret