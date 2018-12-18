# Program that represents cards using a Card class and various functions
# using operator overloading

from copy import copy
'''
Drawpile has a sequence of cards with the top card having the lowest
index and the bottom card having the highest index. 
'''
class Drawpile:
    def __init__(self, cards):
        self.cards = copy(cards)
    # Add card to the bottom of the pile
    def add(self, card):
        self.cards.append(card)
    # Remove the top card and return it
    def draw(self):
        if not self.isEmpty():
            return(self.cards.pop())
        else:
            print("Cannot draw, drawpile is empty!")
    def isEmpty(self):
        return(len(self.cards) == 0)
    # length operator returns the number of cards in the drawpile
    def __len__(self):
        return(len(self.cards))
    def __getitem__(self, index):
        return(self.cards[index])


'''
Card consists of a suit {"Hearts", "Spades", "Clubs", "Diamonds"}
and a value {2,3,4,...,"Jack", "Queen", "King", "Ace"}.
'''
SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
VALUES = {2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,\
    "Jack":10,"Queen":11,"King":12,"Ace":13}
class Card:
    def __init__(self, suit, value):
        if suit in SUITS:
            self.suit = suit
        else:
            print("Error: suit {} not valid".format(suit))
        if value in VALUES:
            self.value = value
        else:
            print("Error: value {} not valid".format(value))

    # Equality operator: cards are equal when they have an equal rank
    def __eq__(self, rhs):
        return (VALUES[self.value] == VALUES[rhs.value])
    def __lt__(self, rhs):
        return (VALUES[self.value] < VALUES[rhs.value])
    def __gt__(self, rhs):
        return (VALUES[self.value] > VALUES[rhs.value])
    def __ge__(self, rhs):
        return (self == rhs or self > rhs)
    def __le__(self, rhs):
        return (self == rhs or self < rhs)

    # Object representation for Card class
    def __repr__(self):
        return ("({}, {})".format(self.suit, self.value))

# Tests Card class
def testCards():
    testCards = [Card("Hearts", 5), Card("Spades", 5), \
        Card("Diamonds", "Ace"), Card("Diamonds", "Jack"),\
        Card("Hearts", 7) ]
    test = Card("Clubs", 7)

    # Test equality operators
    for card in testCards:
        if (test == card):
            print("{} == {}".format(test, card))
        if (test <= card):
            print("{} <= {}".format(test, card))
        if (test < card):
            print("{} < {}".format(test, card))
        if (test > card):
            print("{} > {}".format(test, card))
        if (test >= card):
            print("{} >= {}".format(test, card))

# Test drawpile class
def testDrawpile():
    cards = [Card("Hearts", 5), Card("Spades", 5), \
        Card("Diamonds", "Ace"), Card("Diamonds", "Jack"),\
        Card("Hearts", 7)]
    drawpile = Drawpile(cards)
    drawpile.add(Card("Spades", "Queen"))
    tmp = drawpile.draw()
    print("Number of cards in drawpile: {}".format(len(drawpile)))
    print("Drawn card is {}".format(tmp))


    # Test __getitem__()
    print("\nPrinting all cards in drawpile:")
    for i in range(len(drawpile)):
        print("Card {}: {}".format(i, drawpile[i]))

    # Draw all cards
    empty = False
    while not empty:
        drawpile.draw()

        empty = drawpile.isEmpty()

    # This draw should fail
    drawpile.draw()

    if (drawpile.isEmpty()):
        print("Drawpile is empty")

def main():
    #testCards()
    testDrawpile()

if __name__=="__main__":
    main()