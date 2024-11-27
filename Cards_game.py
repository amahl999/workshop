import random 

option1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]
option2 = [chr(9829), chr(9830), chr(9824), chr(9827)]

combine = list(zip(option1, option2)) #zip or set methods check
random.shuffle(combine)


Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)

Backside = "backside"

a = '''Welkom bij Patrick's pesten spelletje.'''
print(a)

#Give the players 7 cards from the deck each

def player_one():
    intro = print("Player One:")
    return intro


def playerOne():
    players_cards = print(random.choices(option1, k = 7))
    players_cards = print(random.choices(option2, k = 7))
    return players_cards


#shuffle and divide
def suit():
        suit =print(random.choice(option1))
        suit =print(random.choice(option2))
        return suit
        


player_one()
option1[:], option2[:] = zip(*combine)   #print(tuple(combine))
playerOne()



shuffle = input("Press Enter to shuffle ") 

suit()

bet = input("You first. Which card? ") 

if  option1 == bet:
     print("Player 2 is next")
else:
     print("Take 1 card. Player 2 is next ")

def player_two():
    intro = print("Player Two:")
    return intro


def playerTwo():
    players_cards = print(random.choices(option1, k = 7))
    players_cards = print(random.choices(option2, k = 7))
    return players_cards

player_two()
playerTwo()