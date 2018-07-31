from random import randint

# Constants
SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10",\
          "Jack", "Queen", "King"]

def createDeck():
    deck = []
    for suit in SUITS:
        for value in VALUES:
            deck.append((value,suit))
    return deck

# Given a list of cards, returns the cards in a random order
def shuffleDeck(deck):
    randomDeck = []
    while len(randomDeck) < len(deck):
        index = randint(0, len(deck)-1)
        if deck[index] not in randomDeck:
            randomDeck.append(deck[index])
    return randomDeck

