import random 


Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)

Backside = "backside"

#Give the players 7 cards from the deck each

def main():
    intro = print("""Pesten kaartenspel, mede mogelijk gemaakt door ya boy""")
    return intro

#for i in range (0, 6):


def players():
    players_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack", "Joker"]
    players_cards = print(random.choices(players_cards, k = 7))
    return players_cards

    

#shuffle and divide
def suit():
        constants = ["Hearts", "Diamonds", "Spades", "Clubs"]
        constants =print(random.choice(constants))
        

def cards():
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack", "Joker"]
        my_list =print(random.choice(my_list))
        return my_list
        

players()
suit()
cards()

    

