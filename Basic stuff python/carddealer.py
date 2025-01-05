"""https://python.plainenglish.io/draw-a-random-playing-card-in-python-848393d6d868"""

import random

SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def createDeck():
    deck = set()
    for suite in SUITS:
        suiteCards = {f"The {rank} of {suite}" for rank in RANKS}
        deck.update(suiteCards)
    return deck


def main():
    deck = createDeck()
    players = int(input("\nHow many players? >"))
    for index in range(1, players + 1):
        print(f"\nPlayer {index}:")
        for _ in range(7):
            print(deck.pop())

def dealer():
    deck = createDeck()
    dealer = int(input("\nDealerscard: "))
    for i in range(dealer):
        print(f"\nDealer: ")
        for _ in range(1):
            print(deck.pop())



main()
dealer()






