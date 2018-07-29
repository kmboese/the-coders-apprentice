from stringCorrection import *

def main():
    #s = "hello there KEvin, gOOD sir sir. Great saturday, huh?"
    s = '''as it turned out our chance meeting with REverend \
aRTHUR BElling was was to change our whole way of life, and \
every sunday we'd hurry along to St 100NY up the Cream BUn \
and Jam...'''
    print("Original string: \n{}".format(s))
    corrected = correctSentence(s)
    print("\nCorrected string: \n{}".format(corrected))

if __name__ == "__main__":
    main()