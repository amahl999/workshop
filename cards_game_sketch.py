
class Cards:
    def __init__(self, hearts, spades):
        self.hearts = hearts
        self.spades = spades

Card = Cards("King", 8)

print(Card.hearts)
print(Card.spades)