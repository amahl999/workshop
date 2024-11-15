def ask_name():
    name = input("What is your name choom?").capitalize()
    return name

def calculation_expenses(expenses):
    sum_total = sum(expenses)
    return sum_total

exp = [34.5, 67.6, 4598.34, 86.3]

command = input("Which command would you like to run fool? Options: expenses, ask_name ")

if command == "expenses":
    print (calculation_expenses(exp))

elif command == "ask_name":
    ask_name()

else:
    print("invalid command")


#print(calculation_expenses(exp))
#print(ask_name())