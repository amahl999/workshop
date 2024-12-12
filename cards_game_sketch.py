"""Bullying by Pat Pancake"""

import random

# Set up the constants:
HEARTS      = chr(9829)
DIAMONDS    = chr(9830)
SPADES      = chr(9824)
CLUBS       = chr(9827)



# Give the dealer two cards and the player seven cards from the deck each:

deck = getDeck()
dealerHand = [deck.pop(), deck.pop()]
playerHand = [deck.pop(), deck.pop()]

while True:
    displayHands(playerHand, dealerHand, False)
    print()

    # Check if the player has bust:
    if getHandValue(playerHand):
        break

    move = getMove(playerHand)

    if move in ("H"):
        newCard = deck.pop()
        rank, suit = newCard
        print("You drew a {} of {}.".format(rank, suit))
        playerHand.append(newCard)

    if getHandValue(playerHand) > 21:
            #  The player has busted:
            continue
    
    # Handle the dealer's actions:
    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) <= 17:
            # The dealer hits:
            print("Dealer hits....")
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)

            if getHandValue(dealerHand) > 21:
                break # The dealer has busted.
            input("Press Enter to continue....")
            print('\n\n')

        # Show the final hands:
    displayHands(playerHand, dealerHand, True)

     #Show the final hands:
    displayHands(playerHand, dealerHand, True)

    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)
    # Handle whether the player won, lost, or tried:
    if dealerValue > 21:
        print("Dealer busts! You win ${}!")
    elif (playerValue > 21) or (playerValue < dealerValue):
        print("You lost!")
    elif playerValue == dealerValue:
        print("It\'s a tie, the bet is returned to you.")

    input("press Enter to continue....")
    print("\n\n")


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit)) # Add the face and ace cards.
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand): # DOUBLE CHECK FOR BULLYING GAME!!!!!!!!!!!!!!!!!!!!
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False."""
    print()
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER:  ?????")
        # Hide the dealer's first card:
        displayCards(dealerHand[1:])

    # Show the player's cards:
    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"): # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank) # Numbered cards are worth their number.

    # Add the value for the aces:
    value += numberOfAces # Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10
    return value