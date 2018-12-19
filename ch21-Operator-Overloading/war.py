from cards import Card, Drawpile, SUITS, VALUES

DEBUG = False

def dPrint(message):
    if DEBUG:
        print(message)

def main():
    # Game setup
    cards1 = [Card("Diamonds", 2), Card("Hearts", "King"), \
        Card("Clubs", 7)]
    cards2 = [Card("Hearts", 4), Card("Hearts", 3), \
        Card("Spades", 8)]

    # Set up decks
    deck1 = Drawpile(cards1)
    deck2 = Drawpile(cards2)

    print("Deck 1: {}".format(deck1))
    print("Deck 2: {}".format(deck2))

    # Game loop
    while not deck1.isEmpty() and not deck2.isEmpty():
        p1Card = deck1.draw()
        p2Card = deck2.draw()

        # Winning player gets both cards
        if p1Card > p2Card:
            dPrint("Player 1 wins the round!")
            deck1.add(p1Card)
            deck1.add(p2Card)
        # Ignore ties for now
        else:
            dPrint("Player 2 wins the round!")
            deck2.add(p1Card)
            deck2.add(p2Card)
        
        # Print game state
        dPrint("Player 1 deck: {}".format(deck1))
        dPrint("Player 2 deck: {}".format(deck2))

    # Announce winner
    if deck1.isEmpty():
        print("Player 2 wins!")
    elif deck2.isEmpty():
        print("Player 1 wins!")

if __name__=="__main__":
    main()