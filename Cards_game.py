import random 

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "King", "Queen", "Jack", "Joker"]

Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)

Backside = "backside"

a = '''Welkom bij patrick's pesten spelletje.'''
print(a)

#Give the players 7 cards from the deck each

def player_1():
    intro = print("Player One:")
    return intro

player_1()


def players():
    players_cards = print(random.choices(cards, k = 7))
    return players_cards

players()

#shuffle and divide
def suit():
        constants = [chr(9829), chr(9830), chr(9824), chr(9827)]
        constants =print(random.choice(constants))
        

def cards():
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack", "Joker"]
        my_list =print(random.choice(my_list))
        return my_list
        
suit()
cards()

bet = input("You first. Which card? ") 
