import random 

option1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]
option2 = [chr(9829), chr(9830), chr(9824), chr(9827)]

Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)

Backside = "backside"

a = '''Welkom bij Patrick's pesten spelletje.'''
print(a)

#Give the players 7 cards from the deck each

def player_1():
    intro = print("Player One:")
    return intro


def players():
    players_cards = print(random.choices(option1, k = 7))
    players_cards = print(random.choices(option2, k = 7))
    return players_cards


#shuffle and divide
def suit():
        suit =print(random.choice(option1))
        suit =print(random.choice(option2))
        return suit
        

player_1()
players()

shuffle = input("Press Enter to shuffle ") 

suit()

bet = input("You first. Which card? ") 
