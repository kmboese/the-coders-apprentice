from playingCards import *

def testShuffle():
    original = createDeck()
    shuffled = shuffleDeck(original)
    
    assert(len(original) == len(shuffled))
    for card in shuffled:
        assert(card in original)


def main():
    deck = createDeck()
    print("Original deck: {}".format(deck))
    shuffledDeck = shuffleDeck(deck)
    print("Shuffled deck: {}".format(shuffledDeck))

    # Verify that the shuffled deck contains the same cards as the original deck
    testShuffle()
if __name__ == "__main__":
    main()