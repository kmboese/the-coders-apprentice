from playingCards import *

def main():
    deck = createDeck()
    print("Original deck: {}".format(deck))
    shuffledDeck = shuffleDeck(deck)
    print("Shuffled deck: {}".format(shuffledDeck))
if __name__ == "__main__":
    main()