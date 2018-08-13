'''
This program counts how often each letter occurs in a string,
case-insensitively. 

Output: letters with their counts, in order from most to least frequent.
'''
from letterFrequency import *

def testLetterFrequency():
    text = '''Hades arc\nGolden tarp\nBlack hole\nSlack is for\nSlack is for
cutting me\nSlack is for cutting me more.'''
    frequencies = countLetterFrequency(text)
    print("Text is:\n\"{}\"\n\nFrequencies:".format(text))
    printFrequencies(frequencies)

def testSingleLetterFrequency():
    text = '''aAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAAAAaaaaaAaAaaAaAaAaAaAaAaAa'''
    frequencies = countLetterFrequency(text)
    print("Text is: \n\"{}\"\n\nFrequencies:".format(text))
    printFrequencies(frequencies)

def main():
    testLetterFrequency()
    print()
    testSingleLetterFrequency()

if __name__ == "__main__":
    main()