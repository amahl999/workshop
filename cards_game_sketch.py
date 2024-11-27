import random


a = ['Spears', "Adele", "NDubz", "Nicole", "Cristina"]
b = [1,2,3,4,5]
z = zip(a, b)
# => [('Spears', 1), ('Adele', 2), ('NDubz', 3), ('Nicole', 4), ('Cristina', 5)]
random.shuffle(z)
