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
    players = int(input("How many players? >"))
    for index in range(1, players + 1):
        print(f"\nplayer {index}:")
        for _ in range(7):
            print(deck.pop())



if __name__ == "__main__":
    main()




