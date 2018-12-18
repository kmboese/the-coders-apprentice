# Program that represents cards using a Card class and various functions
# using operator overloading

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


    def __repr__(self):
        return ("({}, {})".format(self.suit, self.value))

def main():
    cards = [Card("Hearts", 5), Card("Spades", 5), \
        Card("Diamonds", "Ace"), Card("Diamonds", "Jack") ]
    for i in range(len(cards)-1):
        if (cards[i] == cards[i+1]):
            print("{} == {}".format(cards[i], cards[i+1]))
        if (cards[i] < cards[i+1]):
            print("{} < {}".format(cards[i], cards[i+1]))
        if (cards[i] > cards[i+1]):
            print("{} > {}".format(cards[i], cards[i+1]))


if __name__=="__main__":
    main()