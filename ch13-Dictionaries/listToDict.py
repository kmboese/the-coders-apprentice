# Builds a dictionary from a list of strings as the 
# keys, and the frequency of their occurrence as the
# values.

wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

wordDict = {}

# Build dictionary of keywords and quantities
for word in wordlist:
    if not word in wordDict:
        wordDict[word] = 1
    else:
        wordDict[word] += 1

print(wordDict)