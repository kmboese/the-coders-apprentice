# Converts a comma-separated list of words in a string
# to a dict, with the strings as keys and their 
# frequency as a value

text = "apple,durian,banana,durian,apple,cherry,cherry,mango,"+\
"apple,apple,cherry,durian,banana,apple,apple,apple,"+\
"apple,banana,apple"

textDict = {} # dict that holds strings/frequency key/value pairs
tmp = "" # temporary string

# Convert string to dict

for i in range(len(text)):
    if text[i] == ",":
        if tmp in textDict:
            textDict[tmp] += 1
            tmp = ""
        else:
            textDict[tmp] = 0
            tmp = ""
    else:
        tmp += text[i]

# Print result

print(textDict)